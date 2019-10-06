a = int(input())
i = 0
b = list(map(int,input().split()))
for x in range(a-1):
    for y in range(a-x-1):
        if b[y] > b[y+1]:
            b[y], b[y+1] = b[y+1], b[y]
            i+=1
print(i)
