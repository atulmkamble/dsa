def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        key = input_array[i]
        last_ele_of_sorted_index = i - 1

        while last_ele_of_sorted_index >= 0 and input_array[last_ele_of_sorted_index] > key:
            input_array[last_ele_of_sorted_index + 1] = input_array[last_ele_of_sorted_index]
            last_ele_of_sorted_index -= 1

        input_array[last_ele_of_sorted_index + 1] = key


def main():
    array_to_sort = [5, 4, 3, 2, 1]
    print(f"Input: {array_to_sort}")
    insertion_sort(array_to_sort)
    print(f"Output: {array_to_sort}")


if __name__ == '__main__':
    main()
