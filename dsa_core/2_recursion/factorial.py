def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


def main():
    number = 5
    print(f'Output: {fact(number)}')


if __name__ == '__main__':
    main()
