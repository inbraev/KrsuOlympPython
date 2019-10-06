a = input()
for i in range(len(a)):
    quad = i * i
    listQuad=str(quad)
    dlina = len(listQuad) * -1
    if quad == str(i[::dlina]):
        print(i)
