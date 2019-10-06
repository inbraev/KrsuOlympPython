a = input()
b = list(a)
sum = 0
for i in range(0, len(b), 2):
    sum += int(b[i])
print(sum)
