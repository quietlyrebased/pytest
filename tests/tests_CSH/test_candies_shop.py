import pytest

from main.candies_shop import CandiesShop
from main.exeptions import NoCandiesInShop


@pytest.fixture
def candies():
    candies = {"Lolipop": 20.50, "RotFront": 14, "Petrograd": 17.03}
    return candies


@pytest.fixture
def empry_candies():
    candies = None
    return candies


@pytest.fixture(scope="session")
def hello_tester():
    print("Удачных тестов <3")


@pytest.mark.skipif('config.getoption("--status") == "Закрыт"')
@pytest.mark.usefixtures(
    "hello_tester"
)  # Нужно, когда мы из фикстуры ничего не получаем.
# Просто хотим чтобы она отработала и завершилась.
# Например, почистить БД после других тестов.
class TestCandiesShop:
    @pytest.mark.parametrize(
        "name_candy, result",
        [
            ("Lolipop", 20.50),
            ("RotFront", 14),
            ("Petrograd", 17.03),
        ],
    )
    def test_sell_candies(self, shop_name, candies, name_candy, result):
        shop = CandiesShop(shop_name, candies)
        shop.sell(name_candy)
        assert shop.cash == result

    def test_empry_candies(self, shop_name, empry_candies):
        shop = CandiesShop(shop_name, empry_candies)
        with pytest.raises(NoCandiesInShop):
            shop.sell("Lolipop")
