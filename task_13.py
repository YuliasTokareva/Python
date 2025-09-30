import random

zagadannoe_chislo = random.randint(1, 100)
print("Загадано число от 1 до 100. Угадай!")

while True:
    vvod = input("Введите число: ")
    chislo = int(vvod)

    if chislo == zagadannoe_chislo:
        print("Поздравляю! Ты угадал!")
        break
    elif chislo < zagadannoe_chislo:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")