a, b, c = map(int, input().split())
d = ((b + (b + (a - 1) * c)) * a // 2) // a
print(d)
