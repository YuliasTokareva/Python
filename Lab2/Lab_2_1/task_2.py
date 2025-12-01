s = input("Введите числа через пробел: ")
parts = s.split()

#если ничего не ввели
if len(parts) == 0:
    print("Список пуст.")
else:
    #преобразуем в числа
    numbers = []
    for part in parts:
        try:
            num = float(part)
            numbers.append(num)
        except:
            pass  # пропускаем не числа

    if len(numbers) == 0:
        print("Нет чисел.")
    else:
        print("Список чисел:", numbers)

        # 1-2. Уникальные числа и повторяющиеся числа
        unique = []
        repeating = []
        non_repeating = []
        for x in numbers:
            is_new = True
            for d in non_repeating:
                if x == d:
                    is_new = False
                    break
            if is_new:
                non_repeating.append(x)

        for val in non_repeating:
            count = 0
            for x in numbers:
                if x == val:
                    count = count + 1
            if count == 1:
                unique.append(val)
            else:
                repeating.append(val)
        print("\n1. Уникальные числа:", unique if unique else "нет")
        print("2. Повторяющиеся числа:", repeating if repeating else "нет")

        # 3. Чётные и нечётные (только целые)
        evens = []
        odds = []
        for x in numbers:
            if x == int(x):
                n = int(x)
                if n % 2 == 0:
                    evens.append(n)
                else:
                    odds.append(n)
        print("\n3. Чётные:", evens if evens else "нет")
        print("   Нечётные:", odds if odds else "нет")

        # 4. Отрицательные
        negatives = []
        for x in numbers:
            if x < 0:
                negatives.append(x)
        print("\n4. Отрицательные:", negatives if negatives else "нет")

        # 5. Дробные числа
        floats = []
        for x in numbers:
            if x != int(x):
                floats.append(x)
        print("\n5. Дробные:", floats if floats else "нет")

        # 6. Сумма чисел, кратных 5 (только целые)
        total = 0
        for x in numbers:
            if x == int(x):
                n = int(x)
                if n % 5 == 0:
                    total = total + n
        print("\n6. Сумма чисел, кратных 5:", total)

        # 7. Самое большое число
        max_val = numbers[0]
        i = 1
        while i < len(numbers):
            if numbers[i] > max_val:
                max_val = numbers[i]
            i = i + 1
        print("\n7. Самое большое число:", max_val)

        # 8. Самое маленькое число 
        min_val = numbers[0]
        i = 1
        while i < len(numbers):
            if numbers[i] < min_val:
                min_val = numbers[i]
            i = i + 1
        print("8. Самое маленькое число:", min_val)

