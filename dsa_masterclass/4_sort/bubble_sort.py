def bubble_sort(input_array):
    for iter in range(len(input_array)):
        for i in range(len(input_array) - 1 - iter):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]


array_to_sort = [6, 47, 8, 2, 1]
bubble_sort(array_to_sort)
print(f"Output: {array_to_sort}")
