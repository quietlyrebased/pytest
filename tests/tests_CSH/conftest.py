import pytest


def pytest_addoption(parser):
    parser.addoption("--shopname", action="store", default="Сладкий мир")
    parser.addoption("--status", default="Открыт", choices=("Открыт", "Закрыт"))


@pytest.fixture()
def shop_name(request):
    return request.config.getoption("--shopname")


@pytest.fixture()
def shop_status(request):
    return request.config.getoption("--status")


# Передаётся через команду
# pytest [относительный путь к директории тестов] --[имя параметра]=[значение параметра] -s
# Пример:
# pytest tests/tests_CSH --shopname="Конфетис" -s
