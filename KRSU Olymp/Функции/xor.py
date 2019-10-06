def xor(n, m):
    if n != m:
        print("1")
    else:
        print("0")


a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    xor(n,m)
