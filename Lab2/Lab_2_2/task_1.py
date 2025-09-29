def flatten_list(lst):
    # создаём временный плоский список с помощью рекурсии
    def make_flat(items):
        flat = []
        for x in items:
            if isinstance(x, list):
                flat.extend(make_flat(x))
            else:
                flat.append(x)
        return flat

    # получаем плоскуий
    result = make_flat(lst)

    # очистка
    lst.clear()

    # заполняем его элементами из плоского списка
    for x in result:
        lst.append(x)

# используем пример из условия
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print("Исходный список:", list_a)

flatten_list(list_a)
print("После обработки:", list_a)