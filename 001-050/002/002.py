a, b, sum = 0, 1, 0
while b <= 4000000:
    a, b = b, a + b
    if b % 2 == 0:
        sum += b
print(sum)