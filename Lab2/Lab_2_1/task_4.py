# ввод первого списка
s1 = input("Введите первый набор чисел через пробел: ")
parts1 = s1.split()

# ввод второго списка
s2 = input("Введите второй набор чисел через пробел: ")
parts2 = s2.split()

# преобразуем в числа
list1 = []
for x in parts1:
    list1.append(float(x))

list2 = []
for x in parts2:
    list2.append(float(x))

print("\nПервый список:", list1)
print("Второй список:", list2)

# 1. Числа, которые есть в обоих списках (пересечение)
common = []
for num in list1:
    if num in list2:
        if num not in common:
            common.append(num)

print("\n1. Числа, которые есть в обоих наборах:")
if len(common) == 0:
    print("Нет общих чисел.")
else:
    # выводим целые
    clean_common = []
    for x in common:
        if x.is_integer():
            clean_common.append(int(x))
        else:
            clean_common.append(x)
    print(clean_common)

# 2. Разности
# a) Что есть в первом, но нет во втором
only_in_first = []
for num in list1:
    if num not in list2:
        if num not in only_in_first:
            only_in_first.append(num)

# b) Что есть во втором, но нет в первом
only_in_second = []
for num in list2:
    if num not in list1:
        if num not in only_in_second:
            only_in_second.append(num)

print("\n2. Числа, которые есть только в одном наборе:")
print("   Только в первом:", only_in_first if only_in_first else "нет")
print("   Только во втором:", only_in_second if only_in_second else "нет")

# 3. Все числа из обоих списков, кроме общих
# Это only_in_first + only_in_second
result_part3 = []
for x in only_in_first:
    result_part3.append(x)
for x in only_in_second:
    result_part3.append(x)

print("\n3. Все числа из обоих наборов, кроме общих:")
if len(result_part3) == 0:
    print("Нет таких чисел.")
else:
    clean_part3 = []
    for x in result_part3:
        if x.is_integer():
            clean_part3.append(int(x))
        else:
            clean_part3.append(x)
    print(clean_part3)

