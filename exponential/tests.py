import unittest
from search import esearch

class BinarySearchTestCases(unittest.TestCase):
    def test_search_empty_list(self):
        self.assertFalse(esearch([], 1))

    def test_item_found(self):
        self.assertTrue(esearch([2, 3, 4, 10, 40], 2))
    
    def test_item_not_found(self):
        self.assertFalse(esearch([2, 3, 4, 10, 40 ], 50))

if __name__ == '__main__':
    unittest.main()