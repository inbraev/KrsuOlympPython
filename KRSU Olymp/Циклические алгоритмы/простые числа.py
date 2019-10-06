a, b = map(int, input().split())
for num in range(a, b+1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        print(num)
