def selection_sort(array: list) -> list:
    array = array.copy()

    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    return array
