import random

n = int(input())
a = []
for x in range(n):
    a.append(random.randint(-100, 100))

max_value = max(a)
max_index1 = a.index(max_value)
print(a, sep=" ")
if a.count(max_value) >= 2:
    max_index2 = a.index(max_value, max_index1+1)
    print(max_value, max_index1)
    print(max_value, max_index2)
else:
    print(max_value, max_index1)
    print(-1)

