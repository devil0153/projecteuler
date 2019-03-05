import math

def isPrime(n):
    i = 2
    m = math.sqrt(n)
    while i <= m:
        if n % i == 0:
            return 0
        i += 1
    return 1
i, j = 2, 0
while True:
    if isPrime(i):
        j += 1
        if j == 10001:
            print(i)
            break
    i += 1