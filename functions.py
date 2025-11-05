# functions.py

def add(x, y):
  """Эта функция складывает два числа."""
  return x + y

def get_user_full_name(user_data):
  """Возвращает полное имя пользователя из словаря."""
  first_name = user_data.get("first_name", "")
  last_name = user_data.get("last_name", "")
  return f"{first_name} {last_name}".strip()

def divide(a, b):
  """Делит число a на b."""
  if b == 0:
    raise ValueError("Деление на ноль невозможно")
  return a / b

