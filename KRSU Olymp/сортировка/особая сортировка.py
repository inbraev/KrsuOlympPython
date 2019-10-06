a = int(input())
b = list(map(int, input().split()))
c1 = a // 2
for x in range(c1-1):
    for y in range(c1 - x - 1):
        if b[y] > b[y+1]:
            b[y], b[y+1] = b[y+1], b[y]

for x in range(c1, len(b)-1):
    for y in range(c1, len(b)-1):
        if b[y] < b[y + 1]:
            b[y], b[y + 1] = b[y + 1], b[y]
tmp=''
for i in b:
    tmp+=str(i)+' '
print(tmp[:-1])