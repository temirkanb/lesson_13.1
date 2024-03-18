class Category:
    """класс содержащий название описание и товары"""
    name: 'str'
    overview: 'str'
    goods: 'list'

    category_count = 0
    products = 0

    def __init__(self, name, overview, goods):
        self.name = name
        self.goods = goods
        self.overview = overview

        Category.category_count += 1
        Category.products += len('goods')

    def __repr__(self):
        return (f"Категория - {self.name}, описание - {self.overview},"
                f" продукты - {self.goods}")
