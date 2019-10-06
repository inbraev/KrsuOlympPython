a = input()
b = input()
stop = 0
if '.' not in a:
    print(a + '.' + b)
else:
    a = a.split('.')
    a=a[:-1]
    a='.'.join(a)+'.'+b
    print(a)
