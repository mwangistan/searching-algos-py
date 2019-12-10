import unittest
from search import bsearch

class BinarySearchTestCases(unittest.TestCase):
    def test_search_empty_list(self):
        self.assertFalse(bsearch([], 1))

    def test_item_found(self):
        self.assertTrue(bsearch([1, 'a', '2', 9], '2'))
    
    def test_item_not_found(self):
        self.assertFalse(bsearch([1, 'a', '2', 9], 't'))

if __name__ == '__main__':
    unittest.main()