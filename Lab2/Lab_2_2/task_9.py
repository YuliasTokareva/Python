def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(
                    f"Функция {func.__name__} ожидает {len(expected_types)} аргументов, получено {len(args)}")

            i = 0
            while i < len(args):
                if type(args[i]) != expected_types[i]:
                    raise TypeError(
                        f"Аргумент {i + 1} должен быть {expected_types[i].__name__}, "
                        f"получен {type(args[i]).__name__}"
                    )
                i = i + 1

            result = func(*args, **kwargs)
            print("Результат:", result)
            return result

        return wrapper

    return decorator


@type_check(int, int)
def multiply(a, b):
    return a * b


# основная программа с вводом с клавиатуры
print("Программа умножения двух целых чисел")

try:
    # вводим данные как строки
    input_a = input("Введите первое целое число: ")
    input_b = input("Введите второе целое число: ")

    # преобразуем в целые числа
    num_a = int(input_a)
    num_b = int(input_b)

    # вызываем функцию (декоратор проверит типы)
    multiply(num_a, num_b)

except ValueError:
    print("Ошибка: нужно вводить целые числа!")
except TypeError as e:
    print("Ошибка типов:", e)
