import pytest
from contextlib import (
    nullcontext as does_not_raise,
)  # Для того, чтобы проходили тесты, в которых мы ожидаем ошибку

from main.sticks import LoliPop


class TestCounterStick:
    @pytest.mark.parametrize("count, result", [(1, 2), (2, 3), (-1, 0)])
    def test_counter(self, count, result):
        assert LoliPop().counter(count) == result


class TestStickDeformation:
    @pytest.mark.parametrize(
        "centimeters, result, expectation",
        [
            (7, 20, does_not_raise()),
            (3, 16, does_not_raise()),
            (-3, 10, pytest.raises(ValueError)),
            ("1", 14, pytest.raises(TypeError)),
        ],
    )
    def test_stick_enlarger(self, centimeters, result, expectation):
        with expectation:
            assert LoliPop().stick_enlarger(centimeters) == result

    @pytest.mark.parametrize("centimeters, result", [(3, 10), (10, 3), (0, 13)])
    def test_stick_reducing(self, centimeters, result):
        with pytest.raises(
            ValueError
        ):  # Надо, когда хотим убедиться, что точно получаем эту ошибку
            assert LoliPop().stick_reducing(centimeters) == result
