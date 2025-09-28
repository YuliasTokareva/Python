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

        # 1. Уникальные числа
        unique = []
        for x in numbers:
            found = False
            for u in unique:
                if x == u:
                    found = True
            if not found:
                unique.append(x)
        print("\n1. Уникальные числа:", unique)

        # 2. Повторяющиеся числа
        repeating = []
        for x in numbers:
            count = 0
            for y in numbers:
                if y == x:
                    count = count + 1
            if count > 1:
                already = False
                for r in repeating:
                    if r == x:
                        already = True
                if not already:
                    repeating.append(x)
        if len(repeating) == 0:
            print("\n2. Повторяющиеся числа: нет")
        else:
            print("\n2. Повторяющиеся числа:", repeating)

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

