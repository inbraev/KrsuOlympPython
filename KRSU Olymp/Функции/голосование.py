def election(n):
    if n.count(0) > n.count(1):
        print("0")
    else:
        print("1")


a = int(input())
for i in range(a):
    n = list(map(int, input().split()))
    election(n)
