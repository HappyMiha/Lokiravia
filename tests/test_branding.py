"""Public CLI aliases preserve the same private local workspace and access profile."""
from contextlib import redirect_stdout
from importlib.metadata import EntryPoint
from io import StringIO
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[1]
PROJECT = tomllib.loads((ROOT / 'pyproject.toml').read_text(encoding='utf-8'))['project']


def command(name):
    return EntryPoint(name=name, value=PROJECT['scripts'][name], group='console_scripts').load()


class BrandingCompatibilityTests(unittest.TestCase):
    def test_both_commands_open_the_same_saved_brief_without_moving_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / 'Existing AgentFactory briefs'
            saved = {}

            def serve(app, *, host, port, workers):
                self.assertEqual((host, port, workers), ('127.0.0.1', 8871, 1))
                self.assertEqual(app.title, 'Lokiravia')
                self.assertIn('Lokvetia', app.description)
                with TestClient(app, base_url='http://localhost') as client:
                    profile = client.get('/api/briefs').json()
                    self.assertFalse(profile['build_enabled'])
                    self.assertFalse(profile['publish_enabled'])
                    self.assertFalse(profile['local_ai_enabled'])
                    if not saved:
                        response = client.post('/api/briefs', json={
                            'original_text': 'A moon garden', 'command_id': 'brand-create-0001'})
                        self.assertEqual(response.status_code, 200, response.text)
                        saved.update(response.json())
                    else:
                        response = client.get('/api/briefs/' + saved['id'])
                        self.assertEqual(response.status_code, 200, response.text)
                        self.assertEqual(response.json(), saved)

            with patch.dict('os.environ', {
                'AGENT_FACTORY_API_TOKEN': '', 'AGENT_FACTORY_API_ACTOR': 'Local Creator',
                'AGENT_FACTORY_API_SCOPES': 'read,write', 'AGENT_FACTORY_API_TENANTS': '*',
            }), patch('uvicorn.run', side_effect=serve) as run:
                for name in ('agentfactory-brief', 'lokiravia'):
                    with self.subTest(command=name), patch('sys.argv', [
                        name, '--data', str(directory), '--port', '8871',
                    ]):
                        command(name)()
                self.assertEqual(run.call_count, 2)
            self.assertTrue((directory / 'briefs.sqlite3').is_file())
            self.assertTrue((directory / 'core-intake.sqlite3').is_file())
            self.assertEqual(list(Path(temporary).iterdir()), [directory])

    def test_help_uses_public_name_for_either_entry_point(self):
        for name in ('lokiravia', 'agentfactory-brief'):
            with self.subTest(command=name), patch('sys.argv', [name, '--help']):
                output = StringIO()
                with redirect_stdout(output), self.assertRaises(SystemExit) as stopped:
                    command(name)()
                self.assertEqual(stopped.exception.code, 0)
                self.assertIn('usage: lokiravia', output.getvalue())
                self.assertIn('Lokiravia by Lokvetia', output.getvalue())
                self.assertIn('--data', output.getvalue())

    def test_distribution_identity_is_compatible_with_both_entry_points(self):
        self.assertEqual(PROJECT['name'], 'agentfactory-cloud')
        self.assertIs(command('lokiravia'), command('agentfactory-brief'))
        self.assertEqual(PROJECT['urls']['Homepage'], 'https://lokiravia.com')


if __name__ == '__main__':
    unittest.main()
