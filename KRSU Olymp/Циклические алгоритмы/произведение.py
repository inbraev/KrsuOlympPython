a, b = map(int, input().split())
s = 0
if a < 0 and b < 0:
    for x in range(abs(a)):
        s += b
    s = (abs(s))
if a > 0 and b < 0:
    for x in range(abs(a)):
        s += b
if a < 0 and b > 0:
    for x in range(abs(a)):
        s += b
    s = -s
else:
    for x in range(a):
        s += b

print("{}*({})={}".format(a, b, s))



