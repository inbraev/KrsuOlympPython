a = int(input())
b = list(map(int, input().split()))
maxValue = max(b)
b.sort()
s = sum(b[:-1])
if maxValue < s:
    print("YES")
else:
    print("NO")
