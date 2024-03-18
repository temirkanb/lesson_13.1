from utils import load_json, unpack
import os
from config import ROOT_DIR

PATH_TO_PROD = os.path.join(ROOT_DIR, 'src', 'product.json')


def main():
    list_with_info = load_json(PATH_TO_PROD)
    category_list, products_list = unpack(list_with_info)
    print(category_list)
    print(products_list)


if __name__ == '__main__':
    main()
