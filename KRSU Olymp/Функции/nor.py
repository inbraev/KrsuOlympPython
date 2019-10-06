def nor(n, m):
    if n == m == 0:
        print("1")
    else:
        print("0")


a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    nor(n, m)
