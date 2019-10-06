a, b, c = map(int, input().split())
# Самый старший
if a > b and a > c:
    print("Anton")
elif b > a and b > c:
    print("Boris")
elif c > a and c > b:
    print("Victor")
# Двое старших
elif a > c and a == b:
    print("Victor")
elif a > b and a == c:
    print("Boris")
elif b > a and b == c:
    print("Anton")
# ровесники
else:
    print("Same age")
