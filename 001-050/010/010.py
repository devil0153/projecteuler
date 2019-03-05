import math

def isPrime(n):
    i = 2
    m = math.sqrt(n)
    while i <= m:
        if n % i == 0:
            return 0
        i += 1
    return 1

x, sum = 2, 0
while x < 2000000:
    if isPrime(x):
        sum += x
    x += 1
print(sum)