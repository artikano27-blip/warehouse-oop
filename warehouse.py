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