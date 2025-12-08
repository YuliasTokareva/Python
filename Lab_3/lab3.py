# новогодние игрушки среди его
# свойств должен быть: размер, цвет, форма( еще что-то на свой вкус); среди методов: купить игрушку,
# повесить игрушку на елку, разбить игругку, положить в коробку на хранение, подарить другу
# и всем этим управление через пользовательскую панель, нажал на кнопку сделал нужное действие;
# еще нужно добавить свои собственные исключения
# (например: если игрушка разбилась то ее нельзя подарить, положить на хранение или подарить другу)
class BrokenToyError(Exception):
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

    def buy(self):
        if self.is_bought:
        self.is_bought = True
        print("Игрушка куплена!")

    def hang_on_tree(self):
        if self.is_broken:
            raise BrokenToyError("Нельзя повесить разбитую игрушку!")
        if not self.is_bought:
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



    def gift_to_friend(self):
        if self.is_broken:
            raise BrokenToyError("Разбитую игрушку нельзя подарить!")






def main():
    print("Добро пожаловать в магазин новогодних игрушек!")









if __name__ == "__main__":
    main()






