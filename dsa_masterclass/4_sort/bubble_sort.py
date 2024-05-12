def bubble_sort(input_array):
    for val in range(len(input_array)):
        for i in range(len(input_array) - 1 - val):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
    return input_array


print(f"Output: {bubble_sort([6, 47, 8, 2, 1])}")
