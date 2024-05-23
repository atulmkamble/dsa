def main():
    # Python program to find sum of n natural numbers
    import time
    start = time.time()

    n = 100
    total = 0

    for i in range(1, n + 1):
        total += i

    end = time.time()
    print(f'Total: {total}')
    print(f'Total time {end - start}')


if __name__ == '__main__':
    main()
