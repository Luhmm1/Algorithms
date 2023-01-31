import numpy as np

from sorting.bubble_sort import bubble_sort, optimized_bubble_sort
from sorting.exchange_sort import exchange_sort
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort

def test_already_sorted_arrays():
    for _ in range(50):
        sorted_array = sorted(list(np.random.randint(-100, 100, size=50)))

        assert bubble_sort(sorted_array) == sorted_array
        assert optimized_bubble_sort(sorted_array) == sorted_array
        assert exchange_sort(sorted_array) == sorted_array
        assert insertion_sort(sorted_array) == sorted_array
        assert selection_sort(sorted_array) == sorted_array

def test_already_reverse_sorted_arrays():
    for _ in range(50):
        reverse_sorted_array = sorted(list(np.random.randint(-100, 100, size=50)), reverse=True)
        expected_array = list(reversed(reverse_sorted_array))

        assert bubble_sort(reverse_sorted_array) == expected_array
        assert optimized_bubble_sort(reverse_sorted_array) == expected_array
        assert exchange_sort(reverse_sorted_array) == expected_array
        assert insertion_sort(reverse_sorted_array) == expected_array
        assert selection_sort(reverse_sorted_array) == expected_array

def test_random_arrays():
    for _ in range(100):
        unsorted_array = list(np.random.randint(-100, 100, size=50))
        expected_array = sorted(unsorted_array)

        assert bubble_sort(unsorted_array) == expected_array
        assert optimized_bubble_sort(unsorted_array) == expected_array
        assert exchange_sort(unsorted_array) == expected_array
        assert insertion_sort(unsorted_array) == expected_array
        assert selection_sort(unsorted_array) == expected_array
