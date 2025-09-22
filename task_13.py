import random
zagadannoe_chislo = random.randint(1, 100)
print("Загаданно число от 1 до 100. Угадай.")
# Счётчик попыток
kolichestvo_popitok = 0
# Бесконечный цикл
while True:
    # Пользователь вводит число
    vvod = input("Введите число: ")
    chislo = int(vvod)
    kolichestvo_popitok = kolichestvo_popitok + 1
    print("Попытка номер", kolichestvo_popitok, ". Число:", chislo)
    # Проверяем, угадал ли пользователь
    if chislo == zagadannoe_chislo:
        print("Угадано!")
        print("Колличество попыток:", kolichestvo_popitok)
        break  # выход из цикла

    elif chislo < zagadannoe_chislo:
        print("Загаданное число больше.")

    else:
        print("Загаданное число меньше.")
    print()