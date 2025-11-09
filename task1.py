import numpy as np

# Расходы по месяцам, инд. с 0, номера мес. с 1
expenses = np.array([1200, 1100, 1300, 800, 700, 600, 500, 650, 900, 1000, 1100, 1250])

# Зима
expenses_winter = expenses[[11, 0, 1]]

# Лето
expenses_summer = expenses[[5, 6, 7]]

total_winter = np.sum(expenses_winter)
total_summer = np.sum(expenses_summer)

print(f"Зима: {total_winter} руб.")
print(f"Лето: {total_summer} руб.")

if total_winter > total_summer:
    print("Больше тратится зимой.")
    print(f"Максимальные расходы в месяцах 1, 2, 12")
elif total_summer > total_winter:
    print("Больше тратится летом.")
    print(f"Максимальные расходы в месяцах 6, 7, 8")
else:
    print(f"Расходы одинаковые зимой и летом.")

# Находим индекс месяца с макс. расходами
#ind_max = np.argmax(expenses)
#month_max = ind_max + 1

#print(f"Максимальные расходы в месяце №{month_max}")