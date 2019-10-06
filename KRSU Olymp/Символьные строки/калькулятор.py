def same_signs(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    if first_sign == '*' and second_sign == '*':
        result = first_digit * second_digit * third_digit
    if first_sign == '/' and second_sign == '/':
        result = first_digit // second_digit // third_digit
    if first_sign == '+' and second_sign == '+':
        result = first_digit + second_digit + third_digit
    if first_sign == '-' and second_sign == '-':
        result = first_digit - second_digit - third_digit
    print(result)
    raise SystemExit


def first_divide(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    result = first_digit // second_digit
    if second_sign == '*':
        result *= third_digit
    elif second_sign == '+':
        result += third_digit
    elif second_sign == '-':
        result -= third_digit
    print(result)
    raise SystemExit


def first_multiple(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    result = first_digit * second_digit
    if second_sign == '+':
        result += third_digit
    elif second_sign == '-':
        result -= third_digit
    elif second_sign == '/':
        result //= third_digit
    print(result)
    raise SystemExit


def second_multiple(first_digit, second_digit, third_digit, first_sign, second_sign):
    a = third_digit * second_digit
    if first_sign == '+':
        result = a + first_digit
    elif first_sign == '-':
        result = first_digit - a
    print(result)
    raise SystemExit


def second_divide(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    a = second_digit // third_digit
    if first_sign == '+':
        result = a + first_digit
    elif first_sign == '-':
        result = first_digit - a
    print(result)
    raise SystemExit


def minus_plus(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    result = first_digit - second_digit + third_digit
    print(result)
    raise SystemExit


def plus_minus(first_digit, second_digit, third_digit, first_sign, second_sign):
    result = 0
    result = first_digit + second_digit - third_digit
    print(result)
    raise SystemExit


str = input()
# find indexes of signs

for i in range(len(str) - 1):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        first_sign_index = i + 1
        first_sign = str[i]
        break
for i in range(first_sign_index, len(str) - 1):
    if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
        second_sign_index = i + 1
        second_sign = str[i]
        break

# defining digits by slicing string
first_digit = int(str[0:first_sign_index - 1])
second_digit = int(str[first_sign_index:second_sign_index - 1])
third_digit = int(str[second_sign_index:])
# case when first sign is equal to second sign
if first_sign == second_sign:
    same_signs(first_digit, second_digit, third_digit, first_sign, second_sign)

# first_sign is divide and all varieties with other signs
if first_sign == '/':
    first_divide(first_digit, second_digit, third_digit, first_sign, second_sign)
# first_sign is multiply and all varieties with other signs
if first_sign == '*':
    first_multiple(first_digit, second_digit, third_digit, first_sign, second_sign)
# second_sign is multiply and all varieties with other signs
if second_sign == '*':
    second_multiple(first_digit, second_digit, third_digit, first_sign, second_sign)

# second_sign is divide and all varieties with other signs
if second_sign == '/':
    second_divide(first_digit, second_digit, third_digit, first_sign, second_sign)

# if first_sign minus
if first_sign == '-' and second_sign == '+':
    minus_plus(first_digit, second_digit, third_digit, first_sign, second_sign)

# if first sign plus
if first_sign == '+' and second_sign == '-':
    plus_minus(first_digit, second_digit, third_digit, first_sign, second_sign)
