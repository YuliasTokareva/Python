import time

def cache(func):

    # словарь для хранения кэша
    cache_storage = {}

    def wrapper(*args, **kwargs):
        # преобразуем kwargs в неизменяемый вид: кортеж пар (ключ, значение), отсортированный по ключу
        kwargs_items = []
        for key in kwargs:
            kwargs_items.append((key, kwargs[key]))
        # сортируем по ключу, чтобы порядок не влиял на ключ
        kwargs_items.sort()
        # создаём общий ключ
        cache_key = (args, tuple(kwargs_items))

        # проверяем, есть ли такой ключ в кэше
        if cache_key in cache_storage:
            # возвращаем сохранённый результат
            return cache_storage[cache_key]
        else:
            # вызываем функцию
            result = func(*args, **kwargs)
            # сохраняем результат в кэш
            cache_storage[cache_key] = result
            return result

    return wrapper

# Тестовая функция с "долгим" вычислением
@cache
def slow_multiply(a, b):
    time.sleep(2)  # имитация долгой операции
    return a * b

# первый вызов — функция выполняется
result1 = slow_multiply(3, 4)
print("Результат:", result1)
print()

# второй вызов с теми же аргументами — берётся из кэша
result2 = slow_multiply(3, 4)
print("Результат:", result2)
print()

# вызов с другими аргументами — снова выполняется
result3 = slow_multiply(5, 2)
print("Результат:", result3)
print()

# вызов с именованными аргументами
result4 = slow_multiply(a=3, b=4)
print("Результат:", result4)
print()

# повтор с именованными — из кэша
result5 = slow_multiply(a=3, b=4)
print("Результат:", result5)