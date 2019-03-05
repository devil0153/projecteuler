def isPalindrome(n):
    m = str(n)
    n = len(m)
    for i in range(n // 2):
        if m[i] != m[n -i -1]:
            return 0
    return 1
max = 0
for x in range(999, 1, -1):
    for y in range(x, 1, -1):
        z = x * y
        if isPalindrome(z):
            if max < z:
                max = z
print(max)