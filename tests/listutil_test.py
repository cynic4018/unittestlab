import unittest
from listutil import count_unique, binary_search

class TestCountElement(unittest.TestCase):
    """
    Test count_unique method with borderline cases, typical cases, impossible cases and extreme cases
    """
    def test_empty_case(self):
        list = []
        self.assertEqual(0, count_unique(list))

    def test_one_element_case(self):
        fontlist = ['A']
        mathlist = [1]
        self.assertEqual(1, count_unique(fontlist))
        self.assertEqual(1, count_unique(mathlist))

    def test_no_duplicates_case(self):
        fontlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        mathlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(10, count_unique(fontlist))
        self.assertEqual(10, count_unique(mathlist))


    def test_impossible_case(self):
        list = None
        self.assertIsNone(count_unique(list))


    def test_huge_list_case(self):
        list = []
        for i in range(1,999999):
            list.append(i)

        self.assertEqual(999998, count_unique(list))


class TestBinarySearch(unittest.TestCase):
    """
    Test binary_search method with borderline cases, typical cases, impossible cases and extreme cases
    """
    def test_empty_case(self):
        list = []
        self.assertEqual('List is empty', binary_search(list, 4))

    def test_find_not_found(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual('Not found', binary_search(list, 8))

    def test_element_is_none(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        binary_search(list, None)
        self.assertRaises(TypeError)

    def test_huge_list_case(self):
        list = []
        for i in range(1,999999):
            list.append(i)
        self.assertEqual(49999,binary_search(list, 50000))

if __name__ == "__main__":
    unittest.main()