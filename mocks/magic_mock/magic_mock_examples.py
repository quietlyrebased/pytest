# len(normal_mock_example)  # TypeError

# А вот так Mock не умеет.
# Он не реализует могические методы.
# Для этого нам нужен MagicMock.

# magic_mock_example = MagicMock()

# len(magic_mock_example)  # -> 0, можно настроить
# magic_mock_example[0]  # -> поведёт себя как список или словарь
# str(magic_mock_example)  # -> ок
# iter(magic_mock_example)  # -> ок

# Чтобы настроиь их поведение мы можем его прописать

# magic_mock_example.__len__.return_value = 5
# print(len(magic_mock_example))  # -> 5

# Моки нужны для того, чтобы протестировать нашу логику, а не внешнюю.
# Например:
