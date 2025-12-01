#создаем некоторую структуру в которой будет хранится сделуюзая информация: тема проекта. состав команды которая будет
#выполнять этот проект через пользовательский ввод можно добавить тему
#удалить тему жобавить игроков и ужалить игроков и итоговый вариант должен выводится в файл
n = int(input("Колличество команд:"))
proect = []
for i in range(1, n + 1):
    tema = input(f"Введите тему {i}: ")
    sostav = input(f"Введите состав {i}: ")
    proect.append({
        "тема": tema,
        "состав": sostav
    })

def show_all():
    if not proect:
        print("Список пуст.")
    else:
        print("\n--- Проект ---")
        for i, pro in enumerate(proect, 1):
            print(f"{i}. Тема: {pro['тема']}, Состав: {pro['состав']}")

def find_by_tema(tema):
    for pro in proect:
        if pro["тема"] == tema:
            return pro
    return None

def add_proect():
    tema = input("Тема: ").strip()
    if find_by_tema(tema):
        print("Такая тема  уже существует!")
        return
    sostav = input("Состав: ").strip()
    proect.append({
        "тема": tema,
        "состав": sostav
    })
    print("Добавлено.")

def update_proect():
    tema = input("Тема для изменения: ").strip()
    pro = find_by_tema(tema)
    if not pro:
        print("Не найдено.")
        return
    print(f"Текущие данные: {pro}")
    new_sostav = input("Новый состав (Enter — оставить): ").strip()
    if new_sostav:
        pro["состав"] = str(new_sostav)
    print("Данные обновлены.")

def remove_proect():
    tema = input("Тема для удаления: ").strip()
    for i, pro in enumerate(proect):
        if pro["тема"] == tema:
            del proect[i]
            print("Удалено.")
            return
    print("Не найден.")

def search_proect():
    tema = input("Введите тему для поиска: ").strip()
    pro = find_by_tema(tema)
    if pro:
        print("Найдено:", pro)
    else:
        print("Проект не найден.")


while True:
    print("\n--- Меню ---")
    print("1. Показать все")
    print("2. Найти по теме")
    print("3. Добавить")
    print("4. Изменить")
    print("5. Удалить")
    print("6. Сохранить в файл")
    print("7. Выход")
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
        with open("projects.txt", "w", encoding="utf-8") as f:
            for pro in proect:
                f.write(f"Тема: {pro['тема']},Состав: {pro['состав']}")
        print("Сохранено в projects.txt")
    elif choice == "7":
        print("До свидания!")
        break
    else:
        print("Ничего не найдено. Попробуйте снова.")


