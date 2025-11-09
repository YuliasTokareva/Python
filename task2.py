import numpy as np

# Ввод данных
print("Введите длины участков дороги (через пробел):")
lengths_str = input().strip()

print("Введите средние скорости на участках (через пробел):")
speeds_str = input().strip()

print("Введите номер участка, на котором автомобиль въехал на дорогу:")
k = int(input().strip())

print("Введите номер участка, после проезда которого автомобиль выехал:")
p = int(input().strip())

#  строки в массивы
lengths = np.array(list(map(float, lengths_str.split())))
speeds = np.array(list(map(float, speeds_str.split())))

# проверка: одинаковое ли количество участков и скоростей
if len(lengths) != len(speeds):
    print("Ошибка: количество длин и скоростей не совпадает.")
    exit()

n = len(lengths)  # общее число участков

# проверка k и p
if k < 1 or p < 1:
    print("Ошибка: номера участков должны быть >= 1.")
    exit()
if k > n or p > n:
    print(f"Ошибка: номера участков не должны превышать {n}.")
    exit()
if k > p:
    print("Ошибка: автомобиль не может выехать до въезда (k > p).")
    exit()

# перевод в индексы
start_index = k - 1
end_index = p - 1

#  участки
selected_lengths = lengths[start_index:end_index + 1]
selected_speeds = speeds[start_index:end_index + 1]

#  результаты
S = np.sum(selected_lengths)
T = np.sum(selected_lengths / selected_speeds)
V = S / T

# вывод
print(f"S = {S:.0f} км, T = {T:.2f} час, V = {V:.2f} км/ч")