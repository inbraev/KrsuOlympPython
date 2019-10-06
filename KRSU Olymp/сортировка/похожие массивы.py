a = int(input())
a1 = list(map(int, input().split()))
b = int(input())
b1 = list(map(int, input().split()))
set_a1 = set(a1)
set_b1 = set(b1)
if set_b1.issubset(set_a1) or set_a1.issubset(set_b1):
    print('YES')
else:
    print('NO')



