# ввод первого списка
s1 = input("Введите первый набор чисел через пробел: ")
parts1 = s1.split()

# ввод второго списка
s2 = input("Введите второй набор чисел через пробел: ")
parts2 = s2.split()

# преобразуем в числа и сразу создаём множества
set1 = set()
for x in parts1:
    set1.add(float(x))

set2 = set()
for x in parts2:
    set2.add(float(x))

print("\nПервый набор:", list(set1))
print("Второй набор:", list(set2))

# 1. Числа, которые есть в обоих наборах — пересечение
common = set1 & set2  # можно также: set1.intersection(set2)

# Преобразуем для вывода
common_output = []
for x in common:
    if x.is_integer():
        common_output.append(int(x))
    else:
        common_output.append(x)

print("\n1. Числа, которые есть в обоих наборах:")
if len(common_output) == 0:
    print("Нет общих чисел.")
else:
    print(common_output)

# 2. Разности
only_in_first = set1 - set2    # числа только в первом
only_in_second = set2 - set1   # числа только во втором

# Подготовка вывода только в первом
first_output = []
for x in only_in_first:
    if x.is_integer():
        first_output.append(int(x))
    else:
        first_output.append(x)

# Подготовка вывода только во втором
second_output = []
for x in only_in_second:
    if x.is_integer():
        second_output.append(int(x))
    else:
        second_output.append(x)

print("\n2. Числа, которые есть только в одном наборе:")
print("   Только в первом:", first_output if first_output else "нет")
print("   Только во втором:", second_output if second_output else "нет")

# 3. Все числа из обоих наборов, кроме общих — симметрическая разность
unique_numbers = set1 ^ set2

part3_output = []
for x in unique_numbers:
    if x.is_integer():
        part3_output.append(int(x))
    else:
        part3_output.append(x)

print("\n3. Все числа из обоих наборов, кроме общих:")
if len(part3_output) == 0:
    print("Нет таких чисел.")
else:
    print(part3_output)