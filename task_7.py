# вводим количество секунд
seconds_begin = int(input("Введите количество секунд: "))
print(f"Вы ввели: {seconds_begin} секунд")
minutes = seconds_begin // 60
print(f"Целых минут: {minutes}")
ost_seconds = seconds_begin % 60
print(f"Остаток секунд: {ost_seconds}")
# Вывод
print(f"--- РЕЗУЛЬТАТ ---")
print(f"{seconds_begin} секунд — это {minutes} минут и {ost_seconds} секунд")