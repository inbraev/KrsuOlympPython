import locale

locale.setlocale(locale.LC_ALL, "ru")


a = int(input())
k = a % 10
formatted = locale.format_string("%d", a)
if (a > 9) and (a < 20) or (a > 110) or (k > 4) or (k == 0):
    print("Вам", formatted, "лет.")
else:
    if k == 1:
        print("Вам", formatted, "год.")
    else:
        print("Вам", formatted, "года.")
