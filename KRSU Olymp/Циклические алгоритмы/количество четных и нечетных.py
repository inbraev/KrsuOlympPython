a = input()
b = list(a)
countOdd = 0
countEven = 0
for i in b:
    if int(i) % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(countOdd, countEven)
