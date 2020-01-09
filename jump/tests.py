import unittest
from search import jsearch

class BinarySearchTestCases(unittest.TestCase):
    def test_search_empty_list(self):
        self.assertFalse(jsearch([], 1))

    def test_item_found(self):
        self.assertTrue(jsearch([2, 3, 4, 10, 40], 2))
    
    def test_item_not_found(self):
        self.assertFalse(jsearch([2, 3, 4, 10, 40 ], 50))

if __name__ == '__main__':
    unittest.main()