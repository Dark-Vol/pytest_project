# test_functions.py

import pytest
from functions import add, get_user_full_name, divide

# Базовый тест для функции add
@pytest.mark.math
def test_add():
  """
  Проверяем, что функция add() правильно складывает два числа.
  """
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  assert add(10, -5) == 5

# Тесты без фикстур (для демонстрации проблемы дублирования)
def test_get_user_full_name():
  # Создаем данные для теста
  user = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
  }
  assert get_user_full_name(user) == "John Doe"

def test_user_has_email():
  # Снова создаем те же самые данные!
  user = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
  }
  assert "email" in user

# ШАГ 1: Создаем фикстуру
@pytest.fixture
def sample_user_data():
  """Фикстура, которая возвращает словарь с данными пользователя."""
  return {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
  }

# ШАГ 2: Используем фикстуру в тестах
@pytest.mark.user_profile
def test_get_user_full_name_with_fixture(sample_user_data):
  # Pytest автоматически вызовет фикстуру и передаст ее результат
  # в аргумент sample_user_data
  assert get_user_full_name(sample_user_data) == "Jane Doe"

@pytest.mark.user_profile
def test_user_has_email_with_fixture(sample_user_data):
  assert "email" in sample_user_data

# Параметризация тестов
# Создаем список тестовых сценариев
# Каждый кортеж - это один набор данных: (аргумент_1, аргумент_2, ожидаемый_результат)
test_cases = [
    (1, 2, 3),        # Обычное сложение
    (-1, -1, -2),     # Сложение отрицательных чисел
    (5, 0, 5),        # Сложение с нулем
    (-1, 1, 0),       # Противоположные числа
    (3.5, 2.5, 6.0)   # Сложение чисел с плавающей точкой
]

@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
  """Проверяем функцию add() с разными наборами данных."""
  assert add(a, b) == expected

# Тестирование исключений
def test_divide_by_zero_raises_error():
  """Проверяем, что деление на ноль вызывает ValueError."""
  with pytest.raises(ValueError):
    divide(10, 0)

# @pytest.mark.skip — Пропустить тест
# Используйте этот маркер, если функция еще не реализована или тест зависит от внешних условий, которые сейчас не выполняются.
@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
  # Код теста для новой, еще не готовой функции
  assert False

# @pytest.mark.xfail — Ожидать падения
# Это очень полезно при подходе TDD (Test-Driven Development). Вы нашли баг, написали тест, который его воспроизводит (и который, очевидно, падает), но исправление бага откладывается.
@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
  """Этот тест демонстрирует известную проблему с точностью float в Python."""
  assert (0.1 + 0.2) == 0.3  # Этот тест упадет из-за особенностей float
