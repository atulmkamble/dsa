def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    number = 6
    print(f"Output: {fib(number)}")


if __name__ == '__main__':
    main()
