def merge_sorted_lists(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(list2[j])
            j = j + 1

    while i < len(list1):
        result.append(list1[i])
        i = i + 1

    while j < len(list2):
        result.append(list2[j])
        j = j + 1

    return result

print("Введите первый отсортированный список чисел через пробел:")
input1 = input().strip()
print("Введите второй отсортированный список чисел через пробел:")
input2 = input().strip()

# Преобразуем строки в списки чисел
list1 = []
if input1 != "":
    parts1 = input1.split()
    for part in parts1:
        list1.append(int(part))

list2 = []
if input2 != "":
    parts2 = input2.split()
    for part in parts2:
        list2.append(int(part))

# выполняем слияние
merged = merge_sorted_lists(list1, list2)

# выводим результат
print("\nРезультат объединения:")
print(merged)