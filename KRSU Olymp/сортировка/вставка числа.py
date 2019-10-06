a = int(input())
a1 = list(map(int, input().split()))
val,ind=map(int,input().split())
a1.insert(ind-1,val)
for i in a1:
    print(i,end=' ')