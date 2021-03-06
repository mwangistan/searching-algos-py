import unittest
from search import bsearch, bsearch_rec

class BinarySearchTestCases(unittest.TestCase):
    def test_search_empty_list(self):
        self.assertFalse(bsearch([], 1))

    def test_item_found(self):
        self.assertTrue(bsearch([2, 3, 4, 10, 40], 2))
        self.assertTrue(bsearch_rec([2, 3, 4, 10, 40], 2, 0, 5))
    
    def test_item_not_found(self):
        self.assertFalse(bsearch([2, 3, 4, 10, 40 ], 50))

if __name__ == '__main__':
    unittest.main()