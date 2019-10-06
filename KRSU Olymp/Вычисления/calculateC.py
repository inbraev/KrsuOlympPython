#first solution (run - time error)
# n = input()
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
# d3 = n % 10
# s = "{}, {}, {}".format(d3, d2, d1)
# print(s)

#second solution
s = input()
temp = ''
for i in s:
    temp += i + ", "

print(temp[0: len(temp) - 2])
