from unittest.mock import Mock

import pytest

from mocks.normal_mock.mock_code.bookstore.bookstore import Bookstore
from mocks.normal_mock.mock_code.bookstore.rating_manager import RatingManager
from mocks.normal_mock.mock_code.bookstore.timefixer import TimeFixer


@pytest.fixture()
def time_fixer() -> TimeFixer:
    return Mock(spec=TimeFixer)


# spec= даёт спецификацию: Притворяйся объектом класса TimeFixer
# Теперь замокать метод, который есть у класса можно.
# А вот метод, которого нет - нельзя. time_fixer.new_method.return_value = 42 -> Error


@pytest.fixture()
def rating_manager() -> RatingManager:
    return Mock(spec=RatingManager)


@pytest.fixture
def bookstore(
    time_fixer: TimeFixer,
    rating_manager: RatingManager,
) -> Bookstore:
    return Bookstore(
        name="Книжный магазин Блека",
        capital=50000,
        markup=20,
        discount=5,
        time_fixer=time_fixer,
        rating_manager=rating_manager,
    )


class TestBookstore:
    def test_has_open_date(
        self,
        time_fixer: TimeFixer,
        rating_manager: RatingManager,
    ):
        open_date = "07.07.2027 17:07"
        time_fixer.now.return_value = open_date

        bookstore = Bookstore(
            name="Книжный магазин Блека",
            capital=50000,
            markup=20,
            discount=5,
            time_fixer=time_fixer,
            rating_manager=rating_manager,
        )

        assert bookstore.opening_date == open_date

    def test_has_close_date(
        self,
        bookstore: Bookstore,
        rating_manager: RatingManager,
        time_fixer: TimeFixer,
    ):
        rating_manager.downgrade.return_value = 0

        close_date = "07.07.2027 17:07"
        time_fixer.now.return_value = close_date

        bookstore.availability_book("Джейн Эйр")

        assert bookstore.close_date == close_date
