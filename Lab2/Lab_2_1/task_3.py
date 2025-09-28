s = input("Введите числа через пробел: ")
parts = s.split()

# Переведу строки в числа
numbers = []
for part in parts:
            num = float(part)
            numbers.append(num)
print("Ваши числа:", parts)

# самое большое
max1 = parts[0]
for x in parts:
    if x > max1:
        max1 = x

#список без самого большого числа
parts_bez_max = []
for x in parts:
    if x != max1:
        parts_bez_max.append(x)

#если получился пустой список — значит, все числа были одинаковые
if len(parts_bez_max) == 0:
    print("Второго по величине числа нет.")
else:
    #ищем самое большое в этом новом списке
    max2 = parts_bez_max[0]
    for x in parts_bez_max:
        if x > max2:
            max2 = x

    if max2 == int(max2):
        max2 = int(max2)

    print("Второе по величине число:", max2)