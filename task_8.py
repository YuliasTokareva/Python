#Ввод строки
str = input("Введите строку: ")
print("Вы ввели:", str)
# узнаем длину строки
lenght = len(str)
print("Длина строки:", lenght, "символов")
if lenght <= 1:
    print("Это палиндром! (строка слишком короткая, чтобы не быть палиндромом)")
else:
    if lenght == 2:
        if str[0] == str[1]:
            print("Это палиндром!")
        else:
            print("Это не палиндром.")
    elif lenght == 3:
        if str[0] == str[2]:
            print("Это палиндром!")
        else:
            print("Это не палиндром.")
    elif lenght == 4:
        if str[0] == str[3] and str[1] == str[2]:
            print("Это палиндром!")
        else:
            print("Это не палиндром.")
    elif lenght == 5:
        if str[0] == str[4] and str[1] == str[3]:
            print("Это палиндром!")
        else:
            print("Это не палиндром.")

    else:
        print("Слово должно быть короче")