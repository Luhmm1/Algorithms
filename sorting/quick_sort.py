def _partition(array: list, low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1

    array[i], array[high] = array[high], array[i]

    return i

def _quick_sort(array: list, low: int, high: int) -> list:
    if low >= high:
        return

    pivot_index = _partition(array, low, high)

    _quick_sort(array, low, pivot_index - 1)
    _quick_sort(array, pivot_index + 1, high)


def quick_sort(array: list) -> list:
    array = array.copy()

    _quick_sort(array, 0, len(array) - 1)

    return array
