"""
Algorithm:
we find a value of side by the formula that we used in second task(distance between 2 points)
Finding Perimeter by sum of the sides
Finding half of perimeter
then using Geron's formula calculating square
"""
def findSide(x1, y1, x2, y2):
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = findSide(x1, y1, x2, y2)
b = findSide(x2, y2, x3, y3)
c = findSide(x3, y3, x1, y1)
Perimeter = (a + b + c)
S =abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
print(round(Perimeter,5), S)