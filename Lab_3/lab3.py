# новогодние игрушки среди его
# свойств должен быть: размер, цвет, форма( еще что-то на свой вкус); среди методов: купить игрушку,
# повесить игрушку на елку, разбить игругку, положить в коробку на хранение, подарить другу
# и всем этим управление через пользовательскую панель, нажал на кнопку сделал нужное действие;
# еще нужно добавить свои собственные исключения
# (например: если игрушка разбилась то ее нельзя подарить, положить на хранение или подарить другу)



class BrokenToyError(Exception):
    pass

class InvalidActionError(Exception):
    pass

class Toy:
    def __init__(self, size, color, shape, material):
        self.size = size
        self.color = color
        self.shape = shape
        self.material = material
        self.is_broken = False
        self.is_bought = False
        self.is_on_tree = False
        self.is_in_box = False
        self.is_gifted = False

    def hang_on_tree(self):
        if self.is_broken:
            raise BrokenToyError("Нельзя повесить разбитую игрушку!")
        self.is_on_tree = True
        print("Игрушка повешена на ёлку!")


    def break_toy(self):
        if self.is_broken:
            raise BrokenToyError("Игрушка уже разбита!")
        self.is_broken = True
        self.is_on_tree = False
        self.is_in_box = False
        self.is_gifted = False
        print("Игрушка разбита!")

    def put_in_box(self):
        if self.is_broken:
            raise BrokenToyError("Разбитую игрушку нельзя хранить!")
        if self.is_in_box:
            raise InvalidActionError("Игрушка уже упакована в коробку!")
        self.is_in_box = True
        self.is_on_tree = False
        self.is_gifted = False
        print("Игрушка упакована в коробку!")

    def gift_to_friend(self):
        if self.is_broken:
            raise BrokenToyError("Разбитую игрушку нельзя подарить!")
        if self.is_gifted:
            raise InvalidActionError("Эта игрушка уже была подарена!")
        self.is_gifted = True
        self.is_on_tree = False
        self.is_in_box = False
        print("Игрушка подарена другу!")

    def status(self):
        state = "Куплена"
        if self.is_broken:
            state += ", Разбита"
        elif self.is_on_tree:
            state += ", На ёлке"
        elif self.is_in_box:
            state += ", В коробке"
        elif self.is_gifted:
            state += ", Подарена"
        return f"{self.size}, {self.color}, форма: {self.shape}, материал: {self.material} → {state}"


def main():
    toys = []
    print("Добро пожаловать в магазин новогодних игрушек!")
    while True:
        print("Меню")
        print("1. Купить игрушку.")
        if toys:
            print("2. Повесить игрушку на елку.")
            print("3. Разбить игрушку.")
            print("4. Положить игрушку в коробку.")
            print("5. Подарить игрушку другу.")
            print("6. Показать статус всех игрушек.")
        print("0. Выйти.")

        choice = input("Ваш выбор: ").strip()

        try:
            if choice == "0":
                print("С Новым Годом!")
                break

            elif choice == "1":
                size = input("Размер (маленький/средний/большой): ").strip()
                color = input("Цвет: ").strip()
                shape = input("Форма (шар/звезда/колокольчик): ").strip()
                material = input("Материал (стекло/пластик/дерево): ").strip()
                if not all([size, color, shape, material]):
                    print("Все поля обязательны!")
                    continue
                toys.append(Toy(size, color, shape, material))
                print(f"Поздравляем с покупкой вашей {len(toys)}-й игрушки!")

            elif not toys:
                print("Сначала купите хотя бы одну игрушку!")
                continue

            elif choice == "2":
                num = int(input(f"Номер игрушки (1–{len(toys)}): ")) - 1
                toys[num].hang_on_tree()

            elif choice == "3":
                num = int(input(f"Номер игрушки (1–{len(toys)}): ")) - 1
                toys[num].break_toy()

            elif choice == "4":
                num = int(input(f"Номер игрушки (1–{len(toys)}): ")) - 1
                toys[num].put_in_box()

            elif choice == "5":
                num = int(input(f"Номер игрушки (1–{len(toys)}): ")) - 1
                toys[num].gift_to_friend()

            elif choice == "6":
                print("\nВаши игрушки:")
                for i, toy in enumerate(toys, 1):
                    print(f"{i}. {toy.status()}")

            else:
                print("Неверный выбор.")

        except (ValueError, IndexError):
            print("Ошибка: неверный номер игрушки.")
        except BrokenToyError as e:
            print("Ошибка:", e)
        except InvalidActionError as e:
            print("Невозможно:", e)


if __name__ == "__main__":
    main()






