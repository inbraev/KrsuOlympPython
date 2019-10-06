n = int(input())
aList = list(map(int, input().split()))
aList.sort()
max_value=aList[n-1]
for i in aList:
    try:
        aList.remove(max_value)
    except ValueError:
        break

print(aList[len(aList)-1])
