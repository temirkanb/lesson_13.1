class Category:
    """класс содержащий название описание и товары"""
    name: 'str' or 'int'  # название
    overview: 'str'  # описание
    goods: 'list'  # товары

    category_count = 0
    products = 0

    def __init__(self, name, overview, goods):
        self.name = name
        self.goods = goods
        self.overview = overview

        Category.category_count += 1
        Category.products += len('goods')

    def __repr__(self):
        return (f"Название - {self.name}, Описание - {self.overview},"
                f" Товары - {self.goods}")
