def test_initial(coll):
    coll_for_test = coll.goods[0]
    assert coll_for_test.name == "Lenovo Think T15p"
    assert coll_for_test.overview == "ssd - 1TB, Черный, Процессор Intel® Core, Вес - 2.5кг"
    assert coll_for_test.price == 93000.0
    assert coll_for_test.quantity == 8
