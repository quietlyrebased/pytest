from datetime import datetime

from pydantic import BaseModel
from mocks.normal_mock.mock_code.exeptions import ShopIsClosed


class Book(BaseModel):
    author: str
    price: float


class Bookstore:
    def __init__(self, name: str, capital: float, markup: int = 0, discount: int = 0):
        self.name = name
        self.capital = capital
        self.markup = markup
        self.discount = discount

        self._books: dict[str, Book] = {}
        self._rating: float = 3
        self._regular_customers: set[str] = set()
        self._opening_date = self.current_datetime()
        self._close_date: str | None = None

    def _ensure_active(self) -> None:
        if self._rating == 0:
            raise ShopIsClosed("Магазин больше не работает!")

    def _rating_downgrade(self) -> None:
        self._rating = max(0, self._rating - 0.5)

        if self._rating == 0:
            self._close_date = self.current_datetime()

    def _rating_increase(self) -> None:
        self._rating = min(5, self._rating + 0.1)

    def add_regular_customer(self, name_customer: str) -> None:
        self._regular_customers.add(name_customer)

    def availability_book(self, book_name: str) -> bool:
        """Проверяет наличие книги в магазине."""

        self._ensure_active()

        exist = book_name in self._books

        if not exist:
            self._rating_downgrade()

        return exist

    def availability_author(self, author_name: str) -> bool:
        """Проверяет, есть ли книги данного автора."""

        self._ensure_active()

        exist = any(book.author == author_name for book in self._books.values())

        if not exist:
            self._rating_downgrade()

        return exist

    def add_one_book(
        self,
        author_name: str,
        book_name: str,
        price: float,
    ) -> None:
        """Добавляет одну книгу."""

        self._ensure_active()

        if book_name in self._books:
            raise ValueError("Такая книга уже есть!")
        if self.capital < price:
            raise ValueError("Недостаточно средств!")

        self.capital -= price

        self._books[book_name] = Book(
            author=author_name,
            price=price,
        )

    def _cost_new_books(self, new_books: dict[str, Book]) -> float:
        """Считает стоимость новых книг."""

        return sum(
            book.price for title, book in new_books.items() if title not in self._books
        )

    def add_many_books(
        self,
        new_books: dict[str, Book],
    ) -> None:
        """Добавляет несколько книг."""

        self._ensure_active()

        cost = self._cost_new_books(new_books)
        if self.capital < cost:
            raise ValueError("Недостаточно средств!")
        self.capital -= cost

        for title, book in new_books.items():
            if title not in self._books:
                self._books[title] = book

    def delete_book(self, book_name: str) -> None:
        """Удаляет книгу."""

        self._ensure_active()

        if book_name not in self._books:
            raise ValueError("Такой книги нет!")
        del self._books[book_name]

    def sell_book(self, book_name: str, client: str) -> None:
        """Продаёт книгу."""

        self._ensure_active()

        if book_name not in self._books:
            raise ValueError("Такой книги нет!")

        price = self._books[book_name].price
        price *= 1 + self.markup / 100
        if client in self._regular_customers:
            price *= 1 - self.discount / 100

        self.capital += price

        del self._books[book_name]

        self._rating_increase()

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def opening_date(self) -> str:
        return self._opening_date

    @property
    def close_date(self) -> str | None:
        return self._close_date

    @staticmethod
    def _current_datetime() -> str:
        return datetime.now().strftime("%d.%m.%Y %H:%M")
