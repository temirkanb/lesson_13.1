class Product:
    """класс содержащий название описание цену и количество в наличии"""
    name: 'str'
    overview: 'str'
    price: 'int' or 'float'
    quantity: 'int'

    def __init__(self, name, overview, price, quantity):
        self.name = name
        self.overview = overview
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Продукт - {self.name}, описание - {self.overview}, "
                f"цена - {self.price}, количество в наличие - {self.quantity}")
