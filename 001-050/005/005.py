i = 2521
while True:
    found = True
    for n in range(20, 1, -1):
        if i % n != 0:
            found = False
            break
    if found:
        print(i)
        break
    i += 1