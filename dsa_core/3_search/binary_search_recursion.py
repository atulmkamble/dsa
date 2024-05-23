def binary_search_helper(input_array, left, right, target):
    if left > right:
        return -1

    middle = (left + right) // 2
    middle_element = input_array[middle]

    if middle_element == target:
        return middle
    elif target < middle_element:
        right = middle - 1
        return binary_search_helper(input_array, left, right, target)
    elif target > middle_element:
        left = middle + 1
        return binary_search_helper(input_array, left, right, target)


def binary_search(input_array, target):
    left = 0
    right = len(input_array) - 1
    return binary_search_helper(input_array, left, right, target)


def main():
    print(f"Output: {binary_search([1, 4, 6, 9, 14, 46, 78, 98], 98)}")


if __name__ == '__main__':
    main()
