import json
from src.product import Product
from src.category import Category


def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def unpack(json_list):
    category_list = []
    products_list = []
    for purchase in json_list:
        product_from = []
        for household in purchase.get('goods'):
            product = Product(household['name'], household['overview'],
                              household['price'], household['quantity'])
            product_from.append(product)
        category = Category(purchase['name'], purchase['overview'], product_from)
        category_list.append(category)
        products_list.append(product_from)
    return category_list, products_list
