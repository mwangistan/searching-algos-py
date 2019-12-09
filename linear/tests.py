import unittest
from search import lsearch

class LinearSearchTestCases(unittest.TestCase):
    def test_search_empty_list(self):
        self.assertFalse(lsearch([], 1))

    def test_item_found(self):
        self.assertTrue(lsearch([1, 'a', '2', 9], '2'))
    
    def test_item_not_found(self):
        self.assertFalse(lsearch([1, 'a', '2', 9], 't'))

if __name__ == '__main__':
    unittest.main()