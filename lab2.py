#создаем некоторую структуру в которой будет хранится сделуюзая информация: тема проекта. состав команды которая будет
#выполнять этот проект через пользовательский ввод можно добавить тему
#удалить тему жобавить игроков и ужалить игроков и итоговый вариант должен выводится в файл
n = int(input("Колличество участников команды:"))
r = []
for i in range(1, n + 1):
    tema = input(f"Введите тему {i}: ")
    sostav = input(f"Введите состав {i}: ")
    r.append({
        "тема": tema,
        "состав": sostav
    })


proect = [
    {"тема": "Машинное обучение", "состав": "Маша, Вика, Ксюша"},
    {"тема": "Числовые методы", "состав": "Паша, Даник, Стас"}
]

def show_all():
    if not proect:
        print("Список пуст.")
    else:
        print("\n--- Проект ---")
        for i, pro in enumerate(proect, 1):
            print(f"{i}. {pro['тема']}, {pro['состав']}")

def find_by_tema(tema):
    for pro in proect:
        if pro["Тема"] == tema:
            return pro
    return None

def add_employee():
    tema = input("Тема: ").strip()
    if find_by_tema(tema):
        print("Такая тема  уже существует!")
        return
    sostav = input("Состав: ").strip()
    try:
        proect.append({
            "Тема": tema,
            "Состав": sostav
        })
        print("Добавлено.")
    except ValueError:
        print("Неправильный ввод данных.")

def update_employee():
    tema = input("Тема для изменения: ").strip()
    pro = find_by_tema(tema)
    if not pro:
        print("Не найдено.")
        return
    print(f"Текущие данные: {pro}")
    new_sostav = input("Новая должность (Enter — оставить): ").strip()
    if new_sostav:
        try:
            pro["состав"] = str(new_sostav)
        except ValueError:
            print("Неправильный ввод данных. Не изменено.")
    print("Данные обновлены.")

def remove_employee():
    tema = input("Тема для удаления: ").strip()
    for i, pro in enumerate(proect):
        if pro["тема"] == tema:
            del proect[i]
            print("Удалено.")
            return
    print("Не найден.")

def search_employee():
    tema = input("Введите тему для поиска: ").strip()
    pro = find_by_tema(tema)
    if pro:
        print("Найдено:", pro)
    else:
        print("Сотрудник не найден.")


while True:
    print("\n--- Меню ---")
    print("1. Показать всех")
    print("2. Найти по теме")
    print("3. Добавить")
    print("4. Изменить")
    print("5. Удалить")
    print("6. Выход")
    choice = input("Выбор: ").strip()

    if choice == "1":
        show_all()
    elif choice == "2":
        search_proect()
    elif choice == "3":
        add_proect()
    elif choice == "4":
        update_proect()
    elif choice == "5":
        remove_proect()
    elif choice == "6":
        print("До свидания!")

    elif choice == "7":
        with open("employees.txt", "w", encoding="utf-8") as f:
            for pro in proect:
                f.write(f"{pro['тема']},{pro['состав']}")
        print("Сохранено в employees.txt")
        break
        print("Ничего не найдено.")


