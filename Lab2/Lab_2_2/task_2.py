def merge_dicts(dict_a, dict_b):
    for key in dict_b:
        if key in dict_a:
            if type(dict_a[key]) == dict and type(dict_b[key]) == dict:
                merge_dicts(dict_a[key], dict_b[key])
            else:
                dict_a[key] = dict_b[key]
        else:
            dict_a[key] = dict_b[key]


# Тест
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)