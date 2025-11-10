#структура(сначала сгенерировать скорее всего словарь) для делитедей ( для примера нескольео значений)
#находить в этой стркутуре делители для кокого-то числа
#и вывести все делители для этого числа, это если число уже есть в структуре, если числа еще нет
#сначала добавить через другую структуру и потом уже вывести все делители

divisors_dict = {
    6: [1, 2, 3, 6],
    10: [1, 2, 5, 10],
    15: [1, 3, 5, 15]
}


pending_numbers = [12, 18, 20]


def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def get_divisors(n):
    if n in divisors_dict:
        print(f" Делители числа {n} уже есть: {divisors_dict[n]}")
    elif n in pending_numbers:
        divisors = find_divisors(n)
        divisors_dict[n] = divisors
        pending_numbers.remove(n)
        print(f" Число {n} добавлено. Делители: {divisors}")
    else:
        print(f" Число {n} не найдено и не запланировано к добавлению.")

while True:
    user_input = input("Введите число : ")
    if user_input.lower() == 'выход':
        print("Завершение программы.")
        break
    if not user_input.isdigit():
        print("Пожалуйста, введите корректное целое число.")
        continue
    number = int(user_input)
    get_divisors(number)
















