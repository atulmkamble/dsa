def run(val):
    if val == 0:
        return
    run(val - 1)
    print(val)


n = 10
run(n)
print('Completed')