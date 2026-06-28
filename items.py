class NormalItem():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

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
            raise (f"Ошибка! Цена '{self.name}' не может быть меньше 0 рублей!")
        else:
            self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise (f"Ошибка! Количество товара '{self.name}' не может быть меньше 0 штук!")
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
