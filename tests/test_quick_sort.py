from src.exercise_3_quick_sort import QuickSort


class TestPrime:
    def test_should_not_modify_sorted_array(self):
        array = [1, 2]
        expected = [1, 2]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_not_modify_1_item_array(self):
        array = [1]
        expected = [1]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_sort_positive_numbers(self):
        array = [5, 4, 2, 7]
        expected = [2, 4, 5, 7]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_sort_array_with_negative_number(self):
        array = [5, 4, 2, -7]
        expected = [-7, 2, 4, 5]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_sort_array_with_all_negative_numbers(self):
        array = [-5, -4, -2, -7]
        expected = [-7, -5, -4, -2]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_sort_array_with_0_number(self):
        array = [5, 4, 2, 0, -7]
        expected = [-7, 0, 2, 4, 5]
        QuickSort.quicksort(array)
        assert array == expected

    def test_should_not_modify_empty_array(self):
        array = []
        expected = []
        QuickSort.quicksort(array)
        assert array == expected
