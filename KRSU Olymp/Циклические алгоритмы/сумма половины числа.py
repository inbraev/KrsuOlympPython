a = input()
b = list(a)
sum = 0
if len(b) % 2 != 0:
    for i in range(0,len(b)):
        sum += int(b[i])
else:
    for i in range(0, len(b) // 2, 1):
        sum += int(b[i])
print(sum)
