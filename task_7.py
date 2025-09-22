# вводим количество секунд
seconds_begin = int(input("Введите количество секунд: "))
print("Вы ввели:", seconds_begin, "секунд")
minutes = seconds_begin // 60
print("Целых минут:", minutes)
ost_seconds = seconds_begin % 60
print("Остаток секунд:", ost_seconds)
# Вывод
print("--- РЕЗУЛЬТАТ ---")
print(seconds_begin, "секунд — это", minutes, "минут и", ost_seconds, "секунд")