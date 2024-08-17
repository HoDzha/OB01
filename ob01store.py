# Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.
class Store():
    def __init__(self, name, address):
        self.name = name # - имя магазина
        self.address = address # - адрес магазина
        self.items = {}
    # - инизиализация пустого словаря для items


    def add_item(self, name, price): # - метод добавления nовара в ассортимент
        self.items[name] = price

    def remove_item(self, name): # - метод для удаления товара из ассортимента.
        if name in self.items:
            del self.items[name]

    def get_price(self, name): # - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
        if name in self.items:
            return self.items[name]
        return None



    def update_price(self, name, new_price): # - метод для обновления цены товара.
        if name in self.items:
            self.items[name] = new_price

    def print_price(self):
        print(f"Магазин: {self.name}\nАдрес: {self.address}\nТовары:")
        for name, price in self.items.items():
            print(f"{name}: {price}")
        print("\n")

# создаем магазины

walkmart = Store('Walkmart', 'На деревне у дедушки')
LeroyMarlen = Store('Лерой Марлен', 'Baker street 221b')
azyktuleк = Store('АзыкТулек', ' Beverly Hills, 90210')

# добавляем товары

walkmart.add_item('apple', 11.5)
walkmart.add_item('banana', 2.75)
LeroyMarlen.add_item('молоток', 1.51)
LeroyMarlen.add_item('гвозди', 45.75)
azyktuleк.add_item('Кумыс', 12.5)
azyktuleк.add_item('Учпучмак', 3.2)

LeroyMarlen.update_price('молоток', 11.01)
azyktuleк.remove_item('Кумыс')



# выводим цены
walkmart.print_price()
LeroyMarlen.print_price()
azyktuleк.print_price()