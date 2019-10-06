
aList = list(map(int, input().split()))
aList=aList[1:]
print(*aList,sep=" ")
min_value=min(aList)
j=0
max_value=max(aList)
for o in aList:
    if max_value==o:
        j+=1
for i in range(j):
        aList.insert(aList.index(max(aList)),min_value)
        aList.remove(max(aList))

print(*aList,sep=" ")
