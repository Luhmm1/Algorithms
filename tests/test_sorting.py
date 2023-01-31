import numpy as np

from sorting.bubble_sort import bubble_sort, optimized_bubble_sort

def test_already_sorted_arrays():
    for _ in range(25):
        sorted_array = sorted(list(np.random.randint(-100, 100, size=50)))

        assert bubble_sort(sorted_array) == sorted_array
        assert optimized_bubble_sort(sorted_array) == sorted_array

def test_already_reverse_sorted_arrays():
    for _ in range(25):
        reverse_sorted_array = sorted(list(np.random.randint(-100, 100, size=50)), reverse=True)

        assert bubble_sort(reverse_sorted_array) == list(reversed(reverse_sorted_array))
        assert optimized_bubble_sort(reverse_sorted_array) == list(reversed(reverse_sorted_array))

def test_random_arrays():
    for _ in range(25):
        unsorted_array = list(np.random.randint(-100, 100, size=50))

        assert bubble_sort(unsorted_array) == sorted(unsorted_array)
        assert optimized_bubble_sort(unsorted_array) == sorted(unsorted_array)
