def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


number = 5
print(f'Output: {fact(number)}')
