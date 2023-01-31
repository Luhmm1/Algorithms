def exchange_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

def optimized_exchange_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array) - 1):
        swapped = False

        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                swapped = True
                array[i], array[j] = array[j], array[i]

        if not swapped:
            break

    return array
