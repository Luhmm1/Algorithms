def bubble_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def optimized_bubble_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array) - 1):
        swapped = False

        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]

        if not swapped:
            break

    return array
