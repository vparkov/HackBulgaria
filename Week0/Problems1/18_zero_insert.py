def zero_insert(n):
    str(n)
    length = len(str(n))
    int(n)
    p = [None] * (length)
    for i in range(length - 1, -1, -1):
        p[i] = n % 10
        n //= 10
    r = []
    count = 0 
    for i in range(0, len(p) - 1):
        r.append(p[i])
        if p[i] == p[i + 1] or (p[i] + p[i + 1]) % 10 == 0:
            count += 1
            r.append(0)
    r.append(p[len(p) - 1])

    return r

print(zero_insert(6446))
