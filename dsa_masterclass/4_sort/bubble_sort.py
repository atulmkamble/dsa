def bubble_sort(input_array):
    for iter in range(len(input_array)):
        for i in range(len(input_array) - 1 - iter):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]


def main():
    array_to_sort = [6, 47, 8, 2, 1]
    print(f"Input: {array_to_sort}")
    bubble_sort(array_to_sort)
    print(f"Output: {array_to_sort}")


if __name__ == '__main__':
    main()
