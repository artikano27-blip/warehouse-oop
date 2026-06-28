from items import NormalItem, FragileItem, PerishableItem
from warehouse import Warehouse


# Если этот файл запустили напрямую (кнопкой Run), а не просто импортировали...
if __name__ == "__main__":
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
