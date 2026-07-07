import datetime

import pytest
from unittest.mock import Mock, patch

from mocks.normal_mock.mock_code.holiday_discount import HolidayDiscount


@pytest.fixture
def discount_distributor() -> HolidayDiscount:
    return HolidayDiscount(10)


class TestHolydaiDiscount:
    def test_discount_provided(self, discount_distributor: HolidayDiscount):

        with patch("mocks.when_to_use.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(2026, 1, 11)

            discount_distributor.possibility()
            assert discount_distributor.percentage == 10

    def test_discount_not_provided(self, discount_distributor: HolidayDiscount):
        with patch("mocks.when_to_use.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(2026, 1, 12)

            discount_distributor.possibility()
            assert discount_distributor.percentage == 0


# Мы замокали нужную внешнюю логику, чтобы убедиться что наша логика работает.
# Для этого мы пользуемся связкой with + patch
