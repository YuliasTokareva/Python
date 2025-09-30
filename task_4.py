# вводим сумму
summa = int(input("Введите сумму в рублях: "))
print("Сумма:", summa, "рублей")

# купюры по 100 руб
banknotes_100 = summa // 100
ost = summa % 100

# купюр по 50 руб
banknotes_50 = ost // 50
ost = ost % 50

# купюр по 10 руб
banknotes_10 = ost // 10
ost = ost % 10

# купюр по 5 руб
banknotes_5 = ost // 5
ost = ost % 5

# монет по 2 руб
coin_2 = ost // 2
ost = ost % 2

# монеты по 1 руб
coin_1 = ost

# результат
print("\n--- ИТОГО ---")
print("Для размена суммы", summa, "рублей нужно:")
print("Купюр по 100 руб.:", banknotes_100)
print("Купюр по 50 руб. :", banknotes_50)
print("Купюр по 10 руб. :", banknotes_10)
print("Купюр по 5 руб.  :", banknotes_5)
print("Монет по 2 руб.  :", coin_2)
print("Монет по 1 руб.  :", coin_1)