def doubleFactorial(n):
    fact = 1
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            fact *= i
    else:
        for i in range(1, n + 1, 2):
            fact *= i
    return fact


n = int(input())
answer = doubleFactorial(n)
print(answer)
