import pytest
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def date_time_declaring():
    now_dt = datetime.now()
    format_dt = datetime.strftime(now_dt, "%d.%m.%Y %H:%M")
    print(f"Текущая дата и время: {format_dt}")
