def recursion(counter):
    if counter > 500:
        return 0
    print(f'{counter}: Hello World!')
    recursion(counter + 1)


count = 1
recursion(count)
