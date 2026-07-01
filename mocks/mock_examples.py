from unittest.mock import Mock, MagicMock

normal_mock_example = Mock()

normal_mock_example.some_not_exist_method()

# У Mock есть магический метод __getattr__, который создаёт моки для вызываемых методов на лету.
# Потому нам даже не обязательно его объявлять. Достаточно просто вызвать, всё произойдёт автоматически.

# len(normal_mock_example)  # TypeError

# А вот так Mock не умеет.
# Он не реализует могические методы.
# Для этого нам нужен MagicMock.

magic_mock_example = MagicMock()

len(magic_mock_example)  # -> 0, можно настроить
magic_mock_example[0]  # -> поведёт себя как список или словарь
str(magic_mock_example)  # -> ок
iter(magic_mock_example)  # -> ок

# Чтобы настроиь их поведение мы можем его прописать

magic_mock_example.__len__.return_value = 5
print(len(magic_mock_example))  # -> 5

# Моки нужны для того, чтобы протестировать нашу логику, а не внешнюю.
# Например:
