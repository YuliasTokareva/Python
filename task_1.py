#вводим фамилию
surname = input("Введите фамилию:")
#вводим имя
name = input("Введите имя:")
#вводим отчество
patronymic = input("Введите отчество:")
#после первой буквы имени ставим точку
first_letter_name = name[0]+"."
#после первой буквы отчества ставим точку
first_letter_patronymic = patronymic[0]+"."
#собираем фио
fio = surname + " " + first_letter_name + first_letter_patronymic
print("Ф.И.О.: ")
print(fio)