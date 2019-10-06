def evklidAlgorithm(n, m):
    while n != 0 and m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n + m


n, m = map(int, input().split())
NOD = evklidAlgorithm(n, m)
print("GCD", NOD)
print("LCM", (n * m // NOD))
