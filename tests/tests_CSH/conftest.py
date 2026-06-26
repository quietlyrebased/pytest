import pytest


def pytest_addoption(parser):
    parser.addoption("--shopname", action="store", default="Сладкий мир")


@pytest.fixture()
def shop_name(request):
    return request.config.getoption("--shopname")
