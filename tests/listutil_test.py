import unittest
from listutil import count_unique

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

    # def test_impossible_case(self):
    #     list == None
    #     except:
    #         print("Error list is null")
    #
    #     self.assertEqual("Error list is null", count_unique(list))


    def test_huge_list_case(self):
        list = []
        for i in range(1,999999):
            list.append(i)

        self.assertEqual(999998, count_unique(list))
