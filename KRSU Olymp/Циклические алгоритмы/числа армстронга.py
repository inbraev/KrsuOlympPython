for x in range(100, 999):
    hundreds = x // 100
    ones = x % 10
    tens = (x - hundreds * 100 - ones) // 10
    result = hundreds ** 3 + tens ** 3 + ones ** 3
    if result == x:
        print(x)
