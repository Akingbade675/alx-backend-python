#!/usr/bin/env python3
'''Python Unittests and Integration Tests'''


import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    '''utils.access_nested_map test class'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''test for the utils.access_nested_map function'''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, except_msg):
        '''test that a KeyError is raised for the following inputs'''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(except_msg))


class TestGetJson(unittest.TestCase):
    '''utils.get_json test class'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''test that utils.get_json returns the expected result'''
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''utils.memoize test class'''

    def test_memoize(self):
        '''test the memoize function'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()
        with patch.object(instance, 'a_method', return_value=5) as mock_method:

            self.assertEqual(instance.a_property, 5)
            self.assertEqual(instance.a_property, 5)

            mock_method.assert_called_once()
