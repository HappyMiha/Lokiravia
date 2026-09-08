import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient
from agentfactory_cloud.brief_web import create_app


class SharedIdentityIntegrationTests(unittest.TestCase):
    def test_no_application_user_database_is_created(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {'AGENT_FACTORY_API_TOKEN': 'test-' * 10}):
            os.environ.pop('LOKVETIA_SSO_CLIENT', None)
            with TestClient(create_app(Path(folder)), base_url='http://localhost') as client:
                self.assertFalse(client.get('/auth/session').json()['authenticated'])
                self.assertEqual(client.get('/api/briefs').status_code, 401)
            self.assertFalse((Path(folder) / 'accounts.sqlite3').exists())

    def test_sso_entry_uses_central_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            secret = root / 'client-secret'; secret.write_text('client-secret-' * 4)
            environment = {'AGENT_FACTORY_API_TOKEN': 'test-' * 10, 'LOKVETIA_SSO_CLIENT': 'cloud',
                'LOKVETIA_SSO_ORIGIN': 'https://test.lokiravia.com', 'LOKVETIA_IDENTITY_ORIGIN': 'https://id.lokvetia.com',
                'LOKVETIA_IDENTITY_INTERNAL': 'http://identity.internal', 'LOKVETIA_SSO_SECRET_FILE': str(secret)}
            with patch.dict(os.environ, environment):
                with TestClient(create_app(root), base_url='http://localhost') as client:
                    result = client.get('/auth/sso/start', follow_redirects=False)
                    self.assertEqual(result.status_code, 303)
                    self.assertTrue(result.headers['location'].startswith('https://id.lokvetia.com/authorize?'))
                    self.assertIn('code_challenge=', result.headers['location'])
                    self.assertIn('HttpOnly', result.headers['set-cookie'])
                self.assertFalse((root / 'accounts.sqlite3').exists())


if __name__ == '__main__':
    unittest.main()
