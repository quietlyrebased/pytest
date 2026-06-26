from main.exeptions import NoCandiesInShop


class CandiesShop:

    def __init__(self, name: str, candies: dict | None):
        self.name = name
        self.candies = candies
        self.cash = 0.0

    def add_candy(self, name_candy, coast):
        self.candies[name_candy] = coast
        return self

    def sell(self, name_candy):
        if self.candies is None:
            raise NoCandiesInShop("В магазине нет конфет для продажи")
        self.cash += self.candies[name_candy]
        del self.candies[name_candy]
        return self
