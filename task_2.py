# Исходная строка
line = input("Введите строку: ")
# Строка для результата
newline = ""
# Перебираем каждую букву в строке
for letter in line:
    # Проверяем, НЕ является ли буква гласной
    if letter != "а" and letter != "е" and letter != "ё" and letter != "и" and letter != "о" and letter != "у" and letter != "ы" and letter != "э" and letter != "ю" and letter != "я" and \
       letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
        # Если буква не гласная — добавляем её в новую строку
        newline = newline + letter
# Выводим результат
print("Строка без гласных букв:")
print(newline)