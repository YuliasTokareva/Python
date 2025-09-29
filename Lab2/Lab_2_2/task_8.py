import time

def timing(func):
    def wrapper(*args, **kwargs):
        # запоминаем время начала
        start = time.time()

        # выполняем функцию
        result = func(*args, **kwargs)

        # запоминаем время окончания
        end = time.time()

        # считаем разницу в миллисекундах
        duration_ms = (end - start) * 1000

        # выводим на экран
        print("Функция", func.__name__, "выполнена за", round(duration_ms, 2), "мс")

        return result

    return wrapper
@timing
def example():
    s = 0
    i = 0
    while i < 100000:
        s += i
        i += 1
    return s

example()