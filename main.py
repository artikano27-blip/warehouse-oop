class NormalItem():
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def prepare_for_shipping(self):
        print(f"Товар {self.name} упакован в стандартную коробку")

    def __str__(self):
        return f"Товар: {self.name} | Остаток: {self.quantity} шт. | Цена: {self.price} руб."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            print(f"Ошибка! Цена '{self.name}' не может быть меньше 0 рублей!")
            self.__price = 0
        else:
            self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            print(f"Ошибка! Количество товара '{self.name}' не может быть меньше 0 штук!")
            self.__quantity = 0
        else:
            self.__quantity = quantity


class FragileItem(NormalItem):
    def __init__(self, name, price, quantity, fragility_level):
        super().__init__(name, price, quantity)
        self.fragility_level = fragility_level

    def prepare_for_shipping(self):
        print(f"ВНИМАНИЕ! Товар {self.name} обернут в 3 слоя пупырчатой пленки.")


class PerishableItem(NormalItem):
    def __init__(self, name, price, quantity, expiration_days):
        super().__init__(name, price, quantity)
        self.expiration_days = expiration_days

    def prepare_for_shipping(self):
        print(f"ВНИМАНИЕ! Товар {self.name} помещен в термобокс.\nГоден еще {self.expiration_days} дней!")


class Warehouse():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Товар '{item.name}' добавлен в количестве {item.quantity} штук.")

    def get_total_value(self):
        items_sum = 0
        for item in self.items:
            items_sum += item.quantity * item.price
        print(f"Общая сумма товаров на складе: {items_sum} рублей")


# Создаем Сущность склада
my_warehouse = Warehouse()
# Создаем Сущности товаров
water = NormalItem("Святой Источник 1.5л", price=45, quantity=100)
glasses = FragileItem("Набор бокалов", price=800, quantity=20, fragility_level=4)
milk = PerishableItem("Молоко Простоквашино", price=90, quantity=50, expiration_days=5)
# Принимаем товар
my_warehouse.add_item(water)
my_warehouse.add_item(glasses)
my_warehouse.add_item(milk)
# Отступ для красоты
print()
# Пробегаемся по товарам, готовим к отгрузке
for item in my_warehouse.items:
    print(item)
    item.prepare_for_shipping()
    print("-" * 70)
# Выводим сумму товаров на складе
my_warehouse.get_total_value()
