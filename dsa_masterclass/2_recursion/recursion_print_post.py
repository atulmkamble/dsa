def run(val):
    if val == 0:
        return
    run(val - 1)
    print(val)


def main():
    n = 10
    run(n)
    print('Completed')


if __name__ == '__main__':
    main()
