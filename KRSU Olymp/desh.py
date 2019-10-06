alphabet = {'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
            'H': 7,
            'I': 8,
            'J': 9,
            'K': 10,
            'L': 11,
            'M': 12,
            'N': 13,
            'O': 14,
            'P': 15,
            'Q': 16,
            'R': 17,
            'S': 18,
            'T': 19,
            'U': 20,
            'V': 21,
            'W': 22,
            'X': 23,
            'Y': 24,
            'Z': 25}
list = []
newWord = ''
deshWord = ''
iter = 0
print('Введите слово для шифрования. (Лат. в верхнем регистре)')
word = input()
for search in word:
    if ' ' == search:
        pass
    else:
        print(search, '== []  <= Число для изменение буквы')
        number = int(input())
        list.append([alphabet[search], number])
        summa = sum(list[iter])
        newAlphabet = summa % len(alphabet)
        desh = summa - number
        for x in alphabet:
            if alphabet[x] == newAlphabet:
                newWord += x
        for x in alphabet:
            if alphabet[x] == desh:
                deshWord += x
        iter += 1
print('Ваша зашифрованное слово')
print(newWord)
print(deshWord)
