def unique_elements(nested_list):

    # делаем список плоским
    def flatten(items):
        flat = []
        for item in items:
            if type(item) == list:
                flat.extend(flatten(item))
            else:
                flat.append(item)
        return flat

    all_items = flatten(nested_list)

    # оставить только уникальные
    unique = []
    for element in all_items:
        # проверяем вручную, есть ли уже такой элемент
        found = False
        for u in unique:
            if u == element:
                found = True
                break
        if not found:
            unique.append(element)

    return unique
# теперь вызываем функцию и проверяем результат
test_list = [1, [2, 3], [1, [2, 4, []]], 5]
result = unique_elements(test_list)
print("Уникальные элементы:", result)