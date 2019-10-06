# def numberToBin(n):
#     n = bin(n)
#     get_bin = lambda n : format(n, 'b')
#     print(get_bin(n))


# n = int(input())
# get_bin = lambda n: format(n, 'b')
# print(get_bin(n))
n=int(input())
print(int(bin(n)[2:]))