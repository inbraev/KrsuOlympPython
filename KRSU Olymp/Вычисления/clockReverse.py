clock = int(input())
h = clock // 3600
m = (clock - h * 3600) // 60
s = (clock - m * 60 - h * 3600)
print(h, m, s)
