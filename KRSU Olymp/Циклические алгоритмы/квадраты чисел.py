a, b = map(int, input().split())
for x in range(a, b + 1):
    c = x * x
    print("{}*{}={}".format(x, x, c))
