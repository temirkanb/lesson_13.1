import pytest
import os
from config import ROOT_DIR
from src.product import Product
from src.category import Category


@pytest.fixture
def for_test_load_json():
    return os.path.join(ROOT_DIR, 'src', 'product.json')


@pytest.fixture
def coll():
    return Category("Ноутбуки",
                    "Ноутбук, для работы и повседневной жизни, подходит для пользования почти всех возрастов, "
                    "можно смотреть видео, играть в игры, работать не выходя из дома",
                    [Product("Lenovo Think T",
                             "ssd - 1TB, Черный, Процессор Intel® Core, Вес - 2.5кг",
                             93000.0, 8),
                     Product(
                         "MacBook Air ", "ssd - 2TB, Полуночный черный,"
                                         " Процессор - Apple M2 (8-Core CPU, 10-Core GPU), Вес - 1.5кг",
                         290000.0, 6),
                     Product("Thunderobot Pro",
                             "ssd - 512МB, Игровой, Процессор Intel Core i5 13500H 2.6 ГГц Серый, Вес - 2.1кг",
                             109000.0, 10)])
