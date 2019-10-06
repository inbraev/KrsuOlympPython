a, b, c = map(int, input().split())
print('{0}+{1}+{2}={3}'.format(a, b, c, a+b+c))
print('{0}*{1}*{2}={3}'.format(a, b, c, a*b*c))
average = round((a+b+c)/3,3)
print('({0}+{1}+{2})/3={3}'.format(a, b, c, average))

