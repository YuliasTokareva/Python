print("Число должно быть не больше 99999")
numbers = input("Введите число: ")
print("Число:", numbers)
n = int(numbers) #перевод строки в число
if n % 7 == 0:
    print("Магическое число!")
else:
    s = str(n) #перевод числа обратно в строку
    a = int(s[0]) if len(s) > 0 else 0
    b = int(s[1]) if len(s) > 1 else 0
    c = int(s[2]) if len(s) > 2 else 0
    d = int(s[3]) if len(s) > 3 else 0
    e = int(s[4]) if len(s) > 4 else 0
    print("Сумма цифр:", a + b + c + d + e)