n, a = map(int, input().split())
aList = list(map(int, input().split()))
div = []
for i in aList:
    div.append(i % a)
print(len(set(div)))
