a = input()
toDelete = int(input())
b = list(a)
for i in b[:]:
    if int(i) == toDelete:
        b.remove(i)
print(''.join(b))
