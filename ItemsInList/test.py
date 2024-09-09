import unittest
from ItemList  import count_common_elements


class TestCountCommonElements(unittest.TestCase):

    def test_common_elements(self):
        list1 = [1, 2, 5, 4, 6]
        list2 = [4, 5, 6, 7, 8]
        list3 = [0, 5, 4, 6]
        self.assertEqual(count_common_elements(list1, list2, list3), 3)

    def test_no_common_elements(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = [7, 8, 9]
        self.assertEqual(count_common_elements(list1, list2, list3), 0)

    def test_all_elements_common(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = [1, 2, 3]
        self.assertEqual(count_common_elements(list1, list2, list3), 3)

    def test_empty_list(self):
        list1 = []
        list2 = [1, 2, 3]
        list3 = [1, 2, 3]
        self.assertEqual(count_common_elements(list1, list2, list3), 0)

    def test_single_list(self):
        list1 = [1, 2, 3]
        self.assertEqual(count_common_elements(list1), 3)

    def test_lists_with_duplicates(self):
        list1 = [1, 1, 2, 2, 3, 3]
        list2 = [1, 2, 3, 3]
        list3 = [1, 2, 2, 3]
        self.assertEqual(count_common_elements(list1, list2, list3), 3)


if __name__ == "__main__":
    unittest.main()
