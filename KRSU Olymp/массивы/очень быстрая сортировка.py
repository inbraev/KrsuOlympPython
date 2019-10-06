n=int(input())
aList=[]
for i in range(n):
    aList.append(int(input()))
aList.sort()
print(*aList,sep='\n')