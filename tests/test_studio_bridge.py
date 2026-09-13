from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from agentfactory_cloud.brief_web import create_app


class StudioBridgeTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)

    def create(self, client):
        result = client.post('/api/briefs', json={
            'command_id': 'create-test-studio', 'original_text': 'A cat collects coins.'})
        self.assertEqual(result.status_code, 200, result.text)
        return result.json()

    def test_default_bridge_is_off_and_cannot_launch_any_work(self):
        with patch.dict('os.environ', {'LOKIRAVIA_CORE_WORKSPACE': ''}), TestClient(
                create_app(self.root), base_url='http://127.0.0.1') as client:
            self.assertFalse(client.get('/api/studio/connection').json()['configured'])
            brief = self.create(client)
            self.assertEqual(client.post('/api/briefs/'+brief['id']+'/studio', json={
                'expected_revision': 1, 'confirmed': True}).status_code, 409)

    def test_stale_revision_and_forged_actor_are_refused(self):
        with TestClient(create_app(self.root), base_url='http://127.0.0.1') as client:
            brief = self.create(client)
            url = '/api/briefs/'+brief['id']+'/studio'
            self.assertEqual(client.post(url, json={'expected_revision': 2, 'confirmed': True}).status_code, 409)
            self.assertEqual(client.post(url, json={'expected_revision': 1, 'confirmed': True, 'actor':'other'}).status_code, 422)

    def test_handoff_uses_the_saved_revision_and_session_actor(self):
        with patch.dict('os.environ', {'LOKIRAVIA_CORE_WORKSPACE': str(self.root / 'core')}), TestClient(
                create_app(self.root / 'creator'), base_url='http://127.0.0.1') as client:
            brief = self.create(client)
            with patch('agent_factory.studio_start.create_local_game', return_value={
                    'url':'/studio?mission=test-game', 'mission_id':1}) as start:
                result = client.post('/api/briefs/'+brief['id']+'/studio', json={
                    'expected_revision': 1, 'confirmed': True})
                self.assertEqual(result.status_code, 202, result.text)
                self.assertEqual(start.call_args.kwargs['idea'], brief['original_text'])
                self.assertEqual(start.call_args.kwargs['actor'], client.get('/auth/session').json()['actor'])
                self.assertEqual(result.json()['url'], 'http://127.0.0.1:8765/studio?mission=test-game')

    def test_remote_or_credentialed_core_origins_are_not_accepted(self):
        for url in ['https://example.com', 'http://user:pass@127.0.0.1', 'javascript:alert(1)']:
            with patch.dict('os.environ', {'LOKIRAVIA_CORE_URL':url}), self.assertRaises(ValueError):
                create_app(self.root)


if __name__ == '__main__': unittest.main()
