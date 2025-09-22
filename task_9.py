ip = input("Введите IP-адрес: ")
print("IP:", ip)
# проверяем, сколько точек в строке
many_points = ip.count(".")
print("Количество точек:", many_points)
if many_points != 3:
    print("Ошибка: должно быть ровно 3 точки")
else:
    print("Проверка")
    # разбиваем строку на 4 части по точкам
    parts = ip.split(".")
    print("Части адреса:", parts)  # промежуточная информация
    # Проверяем, что частей ровно 4
    if len(parts) != 4:
        print("Ошибка: должно быть 4 числа, разделённых точками")
    else:
        # каждая часть отдельно
        parts1 = parts[0]
        parts2 = parts[1]
        parts3 = parts[2]
        parts4 = parts[3]
        print("Первая часть:", parts1)
        print("Вторая часть:", parts2)
        print("Третья часть:", parts3)
        print("Четвёртая часть:", parts4)
        # проверка, что каждая часть — это число
        try:
            ch1 = int(parts1)
            ch2 = int(parts2)
            ch3 = int(parts3)
            ch4 = int(parts4)
            print("Проверяем диапазон (0-255)")
            if ch1 >= 0 and ch1 <= 255 and \
               ch2 >= 0 and ch2 <= 255 and \
               ch3 >= 0 and ch3 <= 255 and \
               ch4 >= 0 and ch4 <= 255:
                print("Это корректный IP-адрес!")
            else:
                print("Одно или несколько чисел вне диапазона 0-255")

        except:
            print("Одна из частей — не число. IP-адрес должен содержать только цифры между точками.")