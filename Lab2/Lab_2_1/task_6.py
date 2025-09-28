s = input("Введите элементы через пробел: ")
original = s.split()

print("\nИсходный список:")
print(original)

# создаём новый пустой список
unique = []

print("\nПроверяем каждый элемент:")
for new in original:
    already_exists = False
    for u in unique:
        if u == new:
            already_exists = True
            break

    if already_exists:
        print(f"  '{new}' — уже есть, пропускаем")
    else:
        unique.append(new)
        print(f"  '{new}' — новый, добавляем")

print("\nСписок без дубликатов:")
print(unique)
