def year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
answer = year(n)
print(answer)
