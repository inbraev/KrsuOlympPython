#
# integer=int(input(),16)
# print(format(integer, '0>8b'))


ini_string = input()
res = "{0:08b}".format(int(ini_string, 16))

print(str(res))