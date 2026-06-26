import pytest

from main.candies_shop import CandiesShop


@pytest.fixture
def candies():
    candies = {"Lolipop": 20.50, "RotFront": 14, "Petrograd": 17.03}
    return candies


@pytest.fixture(scope="session")
def hello_tester():
    print("Привет! Удачных тестов <3")


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
    def test_sell_candies(self, candies, name_candy, result):
        shop = CandiesShop("Сладкий мир", candies)
        shop.sell(name_candy)
        assert shop.cash == result
