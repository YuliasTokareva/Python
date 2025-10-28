# Вводим пароль
password = input("Введите пароль: ")
# проверяем длину
lenght = len(password)
print("Длина пароля:", lenght, "символов")
if lenght < 16:
    print("Слишком короткий")
else:
    just_letter = password.isalpha()
    print("Только буквы?", just_letter)
    just_numbers = password.isdigit()
    print("Только цифры?", just_numbers)

    #если хотя бы одно из условий правда — пароль слабый
    if just_letter == True or just_numbers == True:
        print("Слабый пароль")
    else:
        print("Надежный пароль")