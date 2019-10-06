a = input().split()
max_length = 0
for i in a:
    if max_length < len(i):
        max_length = len(i)
        item = i
print(item)
print(max_length)
