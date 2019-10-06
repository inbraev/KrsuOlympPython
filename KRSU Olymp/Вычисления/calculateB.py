

A = input().split()
B = input().split()
x1 = float(A[0])
y1 = float(A[1])
x2 = float(B[0])
y2 = float(B[1])
AB = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5, 3)
print(AB)
