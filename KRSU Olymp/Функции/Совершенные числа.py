# def perfectNumber(n):
#     s = 1
#     for j in range(2, n//2+1):
#         if n % j == 0:
#             s += j
#     if s == n:
#         print("YES")
#     else:
#         print("NO")
#
#
# n = int(input())
# perfectNumber(n)


#a = [a+=s for s in range(2,n//2+1) if n % s == 0]
a=1
n=100
a=[a+s for s in range(2,n//2+1) if n%s==0]
print(a)