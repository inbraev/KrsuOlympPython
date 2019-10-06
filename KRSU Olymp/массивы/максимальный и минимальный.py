# import random
#
# n = int(input())
# a = []
# for x in range(n):
#     a.append(random.randint(-100, 100))
#
# max_value = max(a)
# min_value = min(a)
# max_index = a.index(max_value)
# min_index = a.index(min_value)
# print(*a, sep=" ")
# print("{} {}".format(min_value, min_index))
# print("{} {}".format(max_value, max_index))
# import random
#
# n = int(input())
# a = []
# for x in range(n):
#     a.append(random.randint(-100, 100))
#
# b = a.copy()
# a.sort()
# max_value = a[n-1]
# min_value = a[0]
# max_index = b.index(max_value)
# min_index = b.index(min_value)
# print(*b, sep=" ")
# print("{} {}".format(min_value, min_index))
# print("{} {}".format(max_value, max_index))

import random
import operator
n = int(input())
a = []
for x in range(n):
    a.append(random.randint(-100, 100))
print(*a, sep=" ")

max_index, max_value = max(enumerate(a), key=operator.itemgetter(1))
min_index, min_value = min(enumerate(a), key=operator.itemgetter(1))
print(min_value,min_index)
print(max_value,max_index)