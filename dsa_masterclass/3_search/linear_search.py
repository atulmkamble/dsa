def linear_search(input_array, target):
    for i in range(len(input_array)):
        if input_array[i] == target:
            return i
    return -1


print(f"Output: {linear_search([4, 2, 6, 9, 1], 9)}")
