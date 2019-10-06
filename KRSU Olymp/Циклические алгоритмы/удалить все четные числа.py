a = input()
b = list(a)
for i in b[:]:
    if int(i) % 2 == 0:
        b.remove(i)
print(''.join(b))
