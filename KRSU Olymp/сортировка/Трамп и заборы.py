A = []
n = int(input())
for i in range(n):
    A.append(list(map(str, input().split())))
min_index = [] # indexes of minimal price
min_value = int(A[0][1])
for i in range(n):
    if int(A[i][1]) <= min_value:
        min_index.append(i)
        min_value=int(A[i][1])
max_value_quality = 0
max_index=0
for i in min_index:
    if max_value_quality<int(A[i][2]):
        max_value_quality=int(A[i][2])
        max_index=i
print(A[int(max_index)][0])

