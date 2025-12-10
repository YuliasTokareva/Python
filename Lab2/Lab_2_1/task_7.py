s = input("Введите строку: ")

if s == "":
    print("Строка пустая")
else:
    # начнём с первой буквы
    current_char = s[0]
    count = 1
    result = ""

    i = 1
    while i < len(s):
        # смотрим текущую букву
        letter = s[i]

        # если буква такая же, как предыдущая — увеличиваем счётчик
        if letter == current_char:
            count = count + 1
        else:
            # если буква изменилась — значит, предыдущая закончилась
            # добавляем в результат: букву + сколько раз
            result = result + current_char + str(count)

            # начинаем считать новую букву
            current_char = letter
            count = 1

        i = i + 1  # переходим к следующей букве

    result = result + current_char + str(count)
    print("Сжатая строка:", result)