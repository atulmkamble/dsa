# Python program to find sum of n natural numbers
import time
start = time.time()

n = 100
total = 0

while n > 0:
    total += n
    n -= 1

end = time.time()
print(f'Total: {total}')
print(f'Total time: {end - start}')