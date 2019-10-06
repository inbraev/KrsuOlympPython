n = int(input())
seq = [1, 2, 3, 3, 2, -1, -5, -10]
for i in range(len(seq) - 1, 154):
    seq.append(seq[i - 1] + seq[i - 2] - 2 * seq[i - 3])

print(seq[n - 1])
