import unittest
from dict_map import dict_map

class TestDictMap(unittest.TestCase):

    def test_empty(self):
        value = {}
        func = lambda x: x**2
        actual = dict_map(func, value, True)
        expected = {}
        self.assertEqual(actual, expected)

    def test_shallow(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}}
        func = lambda x: x**2
        actual = dict_map(func, value, False)
        expected = {2:4, 3:9, 4:{5:5, 6:6}}
        self.assertEqual(actual, expected)

    def test_deep(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}}
        func = lambda x: x**2
        actual = dict_map(func, value, True)
        expected = {2:4, 3:9, 4:{5:25, 6:36}}
        self.assertEqual(actual, expected)

    def test_default_deep(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}}
        func = lambda x: x**2
        actual = dict_map(func, value)
        expected = {2:4, 3:9, 4:{5:5, 6:6}}
        self.assertEqual(actual, expected)

    def test_string(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}, 'key': 'key'}
        func = lambda x: x**2
        actual = dict_map(func, value, True)
        expected = {2:4, 3:9, 4:{5:25, 6:36}, 'key': 'key'}
        self.assertEqual(actual, expected)

    def test_dump_func(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}}
        func = lambda x: x
        actual = dict_map(func, value, True)
        expected = {2:2, 3:3, 4:{5:5, 6:6}}
        self.assertEqual(actual, expected)

    def test_undefined_func(self):
        value = {2:2, 3:3, 4:{5:5, 6:6}}
        actual = dict_map(None, value, True)
        expected = {2:2, 3:3, 4:{5:5, 6:6}}
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
