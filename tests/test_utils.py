from src.utils import load_json, unpack


def test_load_json(for_test_load_json):
    assert load_json(for_test_load_json)[1:] == [{
        "name": "Смартфоны",
        "overview": "смартфоны предназначены не только для развлечений,"
                    " но и для облегчения повседневной жизни, смартфон для современного человека это все!",
        "goods": [
            {
                "name": "Apple iPhone",
                "overview": "Память - 512 ГБ, Цвет - титановый, Камера - 48/12/12",
                "price": 167000.0,
                "quantity": 12
            }
        ]
    }]


def test_unpack(for_test_load_json):
    assert unpack(load_json(for_test_load_json))[0][0].name == "Ноутбуки"
