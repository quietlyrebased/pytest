import time

import pytest
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def initial_loading():
    time.sleep(0.5)
    print("Загрузка приветствия...")
    time.sleep(0.5)
    print("Приветствую, Пользователь!\n\nИницилизация процессов...")
    time.sleep(0.5)
    print("Старт тестирования.\nЗапуск тестового модуля...")
    time.sleep(0.5)
    now_dt = datetime.now()
    format_dt = datetime.strftime(now_dt, "%d.%m.%Y %H:%M")
    print(f"Приступаем к тестированию объектов.\nТекущая дата и время: {format_dt}")
    time.sleep(0.5)
