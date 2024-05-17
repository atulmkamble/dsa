def merge(left_result, right_result):
    sorted_array = [None] * (len(left_result) + len(right_result))
    i = j = k = 0
    # 1. Both the arrays have not ended
    while (i < len(left_result)) and (j < len(right_result)):
        if left_result[i] < right_result[j]:
            sorted_array[k] = left_result[i]
            i += 1
        else:
            sorted_array[k] = right_result[j]
            j += 1
        k += 1
    # 2. Left subarray has ended
    while j < len(right_result):
        sorted_array[k] = right_result[j]
        j += 1
        k += 1
    # 3. Right subarray has ended
    while i < len(left_result):
        sorted_array[k] = left_result[i]
        i += 1
        k += 1
    return sorted_array


def merge_sort(input_array):
    # Base condition
    if len(input_array) == 1:
        return input_array

    middle = len(input_array) // 2
    left_subarray = input_array[:middle]
    right_subarray = input_array[middle:]

    left_result = merge_sort(left_subarray)
    right_result = merge_sort(right_subarray)

    return merge(left_result, right_result)


unsorted_array = [4, 3, 6, 7, 8, 2, 1, 9, 5]
output_array = merge_sort(unsorted_array)
print(f"Output: {output_array}")
