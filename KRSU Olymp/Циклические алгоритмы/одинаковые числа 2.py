a = input()
b = list(a)
b.sort()
for x in range(len(b)-1):
    if b[x] == b[x + 1]:
        print("YES")
        break
else:
    print("NO")
