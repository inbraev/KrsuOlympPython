import random

#
#
# def findX(n, x):
#     a = [random.choice([i for i in range(0, 6)]) for j in range(n)]
#     print(a)
#     # c=([i for i in range(len(a)-1) if x==a[i]])
#     # for i in c:
#     #     print(i)
#     for i in range(len(a)-1):
#         if a[i]==x:
#             print(i)


n, x = map(int, input().split())
# findX(n,x)

aList = [random.choice([i for i in range(0, 6)]) for j in range(n)]
indices = [i for i, target in enumerate(aList) if target == x]
print(aList)
for i in indices:
    print(i)
