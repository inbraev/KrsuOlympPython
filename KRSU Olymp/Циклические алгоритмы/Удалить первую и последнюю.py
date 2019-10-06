a = input()
b = list(a)
b = b[1:-1]
for x in range(len(b)):
    if b[0]=='0':
        b.remove('0')
    else:
        break
print(''.join(b))
