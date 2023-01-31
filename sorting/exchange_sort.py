def exchange_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array
