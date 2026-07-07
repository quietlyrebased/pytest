from datetime import datetime


class HolidayDiscount:

    def __init__(self, percentage: int = 0):
        self.percentage = percentage

    def possibility(self) -> bool:
        now = datetime.now()
        if now.month == 1 and now.day <= 11:
            return True
        self.percentage = 0
        return False


# В данном примере нам нужно замокать то, что возвращает datetime.now(), потому что
# Это не наша зона ответственности. Это внешняя логика, которую мы тестировать не будем.
# Наша задача протестировать то, что наш метод possibility работает.
# -> tests/test_discount.py
