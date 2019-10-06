a = int(input())
a1 = list(map(int, input().split()))
for i in range(1, len(a1)):
    string = ''
    temp = a1[i]
    j = i - 1
    while temp <= a1[j] and j >= 0:
        a1[j + 1] = a1[j]
        j = j - 1
        a1[j + 1] = temp
        for t in a1:
            string += str(t) + " "
        print(string)
