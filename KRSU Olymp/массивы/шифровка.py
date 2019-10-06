string = input()
odd = ''
even = ''
for i in range(len(string)):
    if i % 2 == 0:
        even += string[i]
    else:
        odd += string[i]
str = even + odd
count = 0
for i in range(len(string)):
    if string[i] == str[i]:
        count += 1
print(count)

# cccabab
# ccbb
# caa
