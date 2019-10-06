a = int(input())
arr = list(map(int, input().split()))
b = 0
for i in range(a):
    b += arr[i]
print(b)
if 0 in arr or 180 in arr:
    print("NO")
else:
    if b >= (a-2) * 180:
        print("YES")
    else:
        print("NO")
