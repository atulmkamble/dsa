def binary_search(input_array, target):
    left = 0
    right = len(input_array) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = input_array[middle]

        if middle_element == target:
            return middle
        elif target > middle_element:
            left = left + 1
        else:
            right = right - 1

    return -1


def main():
    print(f"Output: {binary_search([1, 5, 7, 39, 76, 98], 98)}")


if __name__ == '__main__':
    main()
