# функция которая будет подсчитывать колличество гласных в строке и соответственно протестируем ее через пай тесты
def count_glasn(text):
    if not isinstance(text, str):
        raise TypeError("Text is not a string")
    glasn = set("aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ")
    count = 0
    for char in text:
        if char in glasn:
            count += 1
    return count
