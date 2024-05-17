def quick_sort(input_array):
    start = 0
    end = len(input_array) - 1
    qs_helper(input_array, start, end)


def qs_helper(input_array, start, end):
    if start >= end:
        return
    pivot = start
    low = start + 1
    high = end

    while low <= high:
        if input_array[low] > input_array[pivot] and input_array[high] < input_array[pivot]:
            input_array[low], input_array[high] = input_array[high], input_array[low]
        if input_array[low] <= input_array[pivot]:
            low += 1
        if input_array[high] >= input_array[pivot]:
            high -= 1

    input_array[high], input_array[pivot] = input_array[pivot], input_array[high]

    # Left subarray
    qs_helper(input_array, start, high - 1)
    # Right subarray
    qs_helper(input_array, high + 1, end)


def main():
    input_array = [4, 3, 2, 5, 1, 9, 7, 6, 8]
    print(f"Input: {input_array}")
    quick_sort(input_array)
    print(f"Output: {input_array}")


if __name__ == '__main__':
    main()
