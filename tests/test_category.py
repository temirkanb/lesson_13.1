from src.category import Category


def test_initial(coll):
    assert coll.name == "Ноутбуки"
    assert coll.overview == ('Ноутбук, для работы и повседневной жизни, подходит для пользования почти всех возрастов,'
                             ' можно смотреть видео, играть в игры, работать не выходя из дома')
    assert coll.goods[0].name == "Lenovo Think T15p"
    assert Category.category_count == 1
    assert Category.products == 5
