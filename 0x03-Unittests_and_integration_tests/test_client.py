#!/usr/bin/env python3
'''Tests for client.GithubOrgClient class'''


import unittest
from unittest.mock import (patch, MagicMock, PropertyMock, Mock)
from typing import Dict
from client import GithubOrgClient
from parameterized import (parameterized, parameterized_class)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''GithubOrgClient Test class'''

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        '''test that GithubOrgClient.org returns the correct value'''
        mock_get_json.return_value = {'org': org_name}
        client = GithubOrgClient(org_name)
        org_url = 'https://api.github.com/orgs/{}'.format(org_name)

        self.assertEqual(client.org, {'org': org_name})
        mock_get_json.assert_called_once_with(org_url)

    def test_public_repos_url(self):
        '''method to unit-test GithubOrgClient._public_repos_url'''

        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/repos'
            }

            result = GithubOrgClient('google')._public_repos_url

            self.assertEqual(result, 'https://api.github.com/repos')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
                        self, repo: Dict[str, Dict],
                        license_key: str, expected_return: bool):
        '''method to unit-test GithubOrgClient.has_license'''
        client_has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(client_has_license, expected_return)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration tests for the GithubOrgClient class'''

    @classmethod
    def setUpClass(cls):
        '''set up'''
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """_summary_
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """_summary_
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls):
        '''tear down'''
        cls.get_patcher.stop()
