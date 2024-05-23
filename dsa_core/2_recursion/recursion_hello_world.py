def recursion(counter):
    if counter > 500:
        return 0
    print(f'{counter}: Hello World!')
    recursion(counter + 1)


def main():
    count = 1
    recursion(count)


if __name__ == '__main__':
    main()
