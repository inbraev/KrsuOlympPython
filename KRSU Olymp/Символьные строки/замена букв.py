a = input()
b = ''
for i in a:
    if i == 'a':
        b += 'b'
    elif i == 'A':
        b += 'B'
    elif i == 'b':
        b += 'a'
    elif i == 'B':
        b += 'A'
    else:
        b+=i
print(b)
