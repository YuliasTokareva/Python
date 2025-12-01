input_str = input("Введите числа через пробел: ")
number_str = input_str.split()

if not number_str:
    print("Пусто.")
else:
    numbers = []
    for s in number_str:
        numbers.append(float(s))

    print("Числа:", numbers)

    max_val = numbers[0]
    second_max_val = None
    for n in numbers:
        if n > max_val:
            second_max_val = max_val
            max_val = n
        elif n < max_val:
            if second_max_val is None or n > second_max_val:
                second_max_val = n

    if second_max_val is None:
        print("Второе по величине число не найдено.")
    else:
        if second_max_val == int(second_max_val):
            second_max_val = int(second_max_val)
        print("Второе по величине число:", second_max_val)