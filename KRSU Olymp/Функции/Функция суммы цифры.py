def sumN(n):
    reverseN=n[::-1]
    sum=0
    for i in n:
        sum+=int(i)
    tmp=''
    for i in reverseN:
        tmp+=i+'+'
    tmp=tmp[:-1]
    tmp+='='
    print(tmp+str(sum))

n=input()
sumN(n)
