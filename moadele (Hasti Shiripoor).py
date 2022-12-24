i = 1
while i <= 10:
    n = int(input("insert your number:"))
    if n >= 5:
        a = 1
        f = 1
        while a != n:
            a += 1
            f = f * a
        if a == n:
            print(f)
            i += 1
    elif n >= 0 and n < 5:
        b = 3 * (n ** 4)
        print(b)
        i += 1
    elif n < 0:
        c = (3 * n) ** 6
        print(c)
        i += 1
