# введите первое число
a = int(input("Введите первое целое число (a): "))
print("число a =", a)
# введите второе число
b = int(input("Введите второе целое число (b): "))
print("число b =", b)
sum = a + b
print("Сумма a + b =", sum)
raznost = a - b
print("Разность a - b =", raznost)
proizvedenie = a * b
print("Произведение a * b =", proizvedenie)
if b == 0:
    print("Частное от деления a / b: на ноль делить нельзя!")
else:
    chastnoe = a / b
    print("Частное от деления a / b =", chastnoe)
if b == 0:
    print("Остаток от деления a % b: на ноль делить нельзя!")
else:
    ost = a % b
    print("Остаток от деления a % b =", ost)
stepen = a ** b
print("a в степени b (a ** b) =", stepen)