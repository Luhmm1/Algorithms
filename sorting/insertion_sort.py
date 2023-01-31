def insertion_sort(array: list) -> list:
    array = array.copy()

    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] <= array[j + 1]:
                break

            array[j], array[j + 1] = array[j + 1], array[j]

    return array
