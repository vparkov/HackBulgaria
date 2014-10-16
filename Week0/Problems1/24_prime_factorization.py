def prime_factorization(n):
    prime_fact = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime_fact.append(d)
            n /= d
        d += 1
    if n > 1:
       prime_fact.append(n)
    return prime_fact

print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
