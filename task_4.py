# вводим сумму
summa = int(input("Введите сумму в рублях: "))
print("Сумму:", summa, "рублей")
# купюры по 100 руб
banknotes_100 = summa // 100
ost = summa % 100
print("Купюр по 100 рублей:", banknotes_100)
print("Остаток после размена 100-рублёвыми:", ost)
# купюр по 50 руб
banknotes_50 = ost // 50
ost = ost % 50
print("Купюр по 50 рублей:", banknotes_50)
print("Остаток после размена 50-рублёвыми:", ost)
# купюр по 10 руб
banknotes_10 = ost // 10
ost = ost % 10
print("Купюр по 10 рублей:", banknotes_10)
print("Остаток после размена 10-рублёвыми:", ost)
# купюр по 5 руб
banknotes_5 = ost // 5
ost = ost % 5
print("Купюр по 5 рублей:", banknotes_5)
print("Остаток после размена 5-рублёвыми:", ost)
# монет по 2 руб
coin_2 = ost // 2
ost = ost % 2
print("Монет по 2 рубля:", coin_2)
print("Остаток после размена 2-рублёвыми:", ost)
# монеты по 1 руб
coin_1 = ost
print("Монет по 1 рублю:", coin_1)
# результат
print("\n--- ИТОГО ---")
print("Для размена суммы", summa, "рублей нужно:")
print("Купюр по 100 руб.:", banknotes_100)
print("Купюр по 50 руб. :", banknotes_50)
print("Купюр по 10 руб. :", banknotes_10)
print("Купюр по 5 руб.  :", banknotes_5)
print("Монет по 2 руб.  :", coin_2)
print("Монет по 1 руб.  :", coin_1)