#создаем некоторую структуру в которой будет хранится сделуюзая информация: тема проекта. состав команды которая будет
#выполнять этот проект через пользовательский ввод можно добавить тему
#удалить тему жобавить игроков и ужалить игроков и итоговый вариант должен выводится в файл
projects = {}

def show_all():
    if not projects:
        print("Список пуст.")
    else:
        print("\n--- Проект ---")
        for i, (tema, members) in enumerate(projects.items(), 1):
            print(f"{i}. Тема: {tema}")
            print(f" Состав: {', '.join(members) if members else '-'}")

def search_project():
    tema = input("Введите тему для поиска: ").strip()
    if tema in projects:
        members = projects[tema]
        print(f"Найдено:\nТема: {tema}\nСостав: {', '.join(members) if members else '-'}")
    else:
        print("Проект с такой темой не найден.")

def add_project():
    tema = input("Тема для нового проекта: ").strip()
    if tema in projects:
        print("Такая тема  уже существует!")
        return
    sostav_str = input("Состав команды (через запятую): ").strip()
    members = [name.strip() for name in sostav_str.split(',') if name.strip()]
    projects[tema] = members
    print("Добавлено.")

def manage_team():
    tema = input("Тема: ").strip()
    if tema not in projects:
        print("Не найдено.")
        return
    while True:
        print(f"\n --- Состав проекта: {tema} ---")
        members = projects[tema]
        if members:
            for i, name in enumerate(members, 1):
                print(f"{i}. {name}")
        else:
            print("Ничего не найдено.")

        print("\n1. Добавить участника")
        print("2. Удалить участника")
        print("3. Назад")
        choice = input("Выбор: ").strip()

        if choice == "1":
            name = input("Имя нового участника: ").strip()
            if name in members:
                print("Этот участник уже в команде")
            else:
                members.append(name)
                print(f"Участник: {name} добавлен.")

        elif choice == "2":
            name = input("Имя участника для удаления: ").strip()
            if name in members:
                members.remove(name)
                print(f"Участник: {name} удален.")
            else:
                print("Такого участника нет в команде.")

        elif choice == "3":
            break
        else:
            print("Неверный выбор.")

def remove_project():
    tema = input("Тема для удаления: ").strip()
    if tema in projects:
        del projects[tema]
        print("Удалено.")
    else:
        print("Не найден.")

def save_project():
    if not projects:
        print("Нет данных для сохранения.")
        return
    with open("projects.txt", "w", encoding="utf-8") as f:
        for tema, members in projects.items():
            f.write(f"Тема: {tema}")
            f.write(f"Состав: {', '.join(members) if members else '-'}")
    print("Сохранено в projects.txt")

while True:
    print("\n--- Меню ---")
    print("1. Показать все")
    print("2. Найти по теме")
    print("3. Добавить новый проект")
    print("4. Изменить состав команды")
    print("5. Удалить")
    print("6. Сохранить в файл")
    print("7. Выход")
    choice = input("Выбор: ").strip()
    if choice == "1":
        show_all()
    elif choice == "2":
        search_project()
    elif choice == "3":
        add_project()
    elif choice == "4":
        manage_team()
    elif choice == "5":
        remove_project()
    elif choice == "6":
        save_project()
    elif choice == "7":
        print("До свидания!")
        break
    else:
        print("Ничего не найдено. Попробуйте снова.")


