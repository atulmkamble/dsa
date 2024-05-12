def selection_sort(input_array):
    for i in range(len(input_array)):
        min_val_index = i
        for j in range(i + 1, len(input_array)):
            if input_array[j] < input_array[min_val_index]:
                min_val_index = j
        input_array[i], input_array[min_val_index] = input_array[min_val_index], input_array[i]


array_to_sort = [99, 54, 35, 22, 9, 2, 2]
selection_sort(array_to_sort)
print(f"Output: {array_to_sort}")
