
n = int(input())
aList=[]
aList=(list(map(int, input().split())))
max_value = max(aList)

print(max_value, aList.count(max_value))
