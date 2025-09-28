word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# приведём к нижнему регистру
w1 = word1.lower()
w2 = word2.lower()

print(f"\nПривели к нижнему регистру:")
print(f"Первое: '{w1}'")
print(f"Второе: '{w2}'")

# проверим длину
if len(w1) != len(w2):
    print("\nДлины разные - это НЕ анаграммы.")
    result = False
else:
    # преобразуем слова в списки букв
    letters1 = []
    for ch in w1:
        letters1.append(ch)

    letters2 = []
    for ch in w2:
        letters2.append(ch)

    print("\nПреобразовали слова в списки букв:")
    print("Первое:", letters1)
    print("Второе:", letters2)
    print()

    # для каждой буквы из первого слова найдём такую же во втором и удалим
    all_found = True
    i = 0
    while i < len(letters1):
        ch = letters1[i]
        # ищем эту букву во втором списке
        found = False
        j = 0
        while j < len(letters2):
            if letters2[j] == ch:
                # если находим удоляем по индексу
                del letters2[j]
                found = True
                break
            j = j + 1

        if not found:
            all_found = False
            break

        i = i + 1

    if all_found and len(letters2) == 0:
        result = True
        print("\nВсе буквы совпали!")
    else:
        result = False
        print("\nНе все буквы из первого слова есть во втором.")

# Вывод результата
print("\nРезультат проверки:")
if result:
    print("True - слова являются анаграммами!")
else:
    print("False - слова не являются анаграммами.")