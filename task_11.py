day = int(input("Введите день рождения: "))
print("Дата:", day)
month = int(input("Введите месяц рождения: "))
print("Месяц:", month)
# Определяем знак зодиака
if month == 1:
    if day <= 19:
        znak = "Capricorn"
    else:
        znak = "Aquarius"

elif month == 2:
    if day <= 18:
        znak = "Aquarius"
    else:
        znak = "Pisces"

elif month == 3:
    if day <= 20:
        znak = "Pisces"
    else:
        znak = "Aries"

elif month == 4:
    if day <= 19:
        znak = "Aries"
    else:
        znak = "Taurus"

elif month == 5:
    if day <= 20:
        znak = "Taurus"
    else:
        znak = "Gemini"

elif month == 6:
    if day <= 20:
        znak = "Gemini"
    else:
        znak = "Cancer"

elif month == 7:
    if day <= 22:
        znak = "Cancer"
    else:
        znak = "Leo"

elif month == 8:
    if day <= 22:
        znak = "Leo"
    else:
        znak = "Virgo"

elif month == 9:
    if day <= 22:
        znak = "Virgo"
    else:
        znak = "Libra"

elif month == 10:
    if day <= 22:
        znak = "Libra"
    else:
        znak = "Scorpio"

elif month == 11:
    if day <= 21:
        znak = "Scorpio"
    else:
        znak = "Sagittarius"

elif month == 12:
    if day <= 21:
        znak = "Sagittarius"
    else:
        znak = "Capricorn"

else:
    znak = "Ошибка: неверный месяц"
print("--- РЕЗУЛЬТАТ ---")
print("Ваш знак зодиака:", znak)