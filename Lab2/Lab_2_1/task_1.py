text = input("Введите текст: ")

#делаем все буквы маленькими, чтобы 'Apple' и 'apple' были одинаковые
text = text.lower()

#split сам уберёт все лишние пробелы
words = text.split()

#создаём пустой словарь, чтобы считать слова
slovar = {}

#проходим по каждому слову в списке
for word in words:
    #увеличиваем счётчик если слово уже в словаре
    if word in slovar:
        slovar[word] = slovar[word] + 1
        #если слова ещё нет — добавляем его со счётчиком 1
    else:
        slovar[word] = 1

print()
print("Слова и сколько раз они встречаются:")
print(slovar)

#считаем, сколько уникальных слов
kolvo_unikalnih = len(slovar)
print("Количество уникальных слов:", kolvo_unikalnih)