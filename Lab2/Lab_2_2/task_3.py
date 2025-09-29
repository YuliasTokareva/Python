# нам нужен модуль datetime, чтобы узнать текущее время
import datetime

def log_calls(log_file):
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            # получаем текущее время: год-месяц-день часы:минуты:секунды
            current_time = datetime.datetime.now()
            # преобразуем в строку: %Y=год, %m=месяц, %d=день, %H=часы, %M=минуты, %S=секунды
            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

            func_name = original_function.__name__

            # собираем аргументы
            arguments = []
            i = 0
            while i < len(args):
                arguments.append(repr(args[i]))
                i = i + 1
            for key in kwargs:
                arguments.append(key + "=" + repr(kwargs[key]))

            if len(arguments) == 0:
                args_str = ""
            else:
                args_str = ", ".join(arguments)

            # строка для записи
            log_line = time_str + " — вызвана функция " + func_name + " с аргументами (" + args_str + ")\n"

            # записываем в файл
            f = open(log_file, "a", encoding="utf-8")
            f.write(log_line)
            f.close()

            return original_function(*args, **kwargs)

        return wrapper

    return decorator
@log_calls("test_log.txt")
def hello():
    print("Функция работает!")
hello()
