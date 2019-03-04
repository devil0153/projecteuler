import math

def isPrime(n):
    i = 2
    m = math.sqrt(n)
    while i <= m:
        if n % i == 0:
            return 0
        i += 1
    return 1

x = 600851475143
y = math.sqrt(x)
z = math.floor(y)
while z > 1:
    if x % z == 0:
        if isPrime(z) == 1:
            print(z)
            break
    z -= 1