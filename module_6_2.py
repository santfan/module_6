class Vehicle:

  '''Класс Транспортное средство принимает аргументы:
  1. Имя владельца - name_owner
  2. Марка модели - model
  3. Цвет модели - color
  4. Мощность двигателя - engine_power
  Автомобиль может менять владельца
  Цвет автомобиля можно менять только на цвета из списка __COLOR_VARIANTS
  остальные параметры задаются при создании и изменению НЕ ПОДЛЕЖАТ! '''

  __COLOR_VARIANTS = ['braun', 'red', 'orange', 'black', 'white']

  def __init__(self, name_owner, model, color, engine_power):
    # При инициации учтем неизменяеость аргументов
    self.__model = model
    self.__engine_power = engine_power
    self.__color = color
    # Параметр Владелец можно изменять
    self.name_owner = name_owner

  # Функция получения Марки
  def get_model(self):
    return f'Модель: {self.__model}'

  # Функция получения Мощности
  def get_horsepower(self):
    return f'Мощность двигателя: {self.__engine_power}'

  # Функция получения Цвета
  def get_color(self):
    return f'Цвет: {self.__color}'

  # Функция вывода информации о транспортном средстве
  def print_info(self):
    print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}')
    print('Владелец: ', self.name_owner)

  # Функция изменения цвета
  def set_color(self, new_color):
    # Функция провеки разрешенных цветов
    if new_color.lower() in self.__COLOR_VARIANTS:
      self.__color = new_color
    else:
      print(f'Нельзя изменить цвет на {new_color}')

# Создадим дочерний класс Транспортоного средства Sedan
class Sedan(Vehicle):
  # Ограничения пассажирских мест для Sedan
  __PASSENGERS_LIMIT = 5

print(Vehicle.__doc__)

# Создадим экземпляр класса Транспортное средство СЕДАН
# Экземпяр Sedan наследует атрибуты родительского класса Vehicle
vehicle1 = Sedan('Fedos','Toyota Mark II', 'blue', 500)

# Проверим создание
vehicle1.print_info()

# Попытаемся изменить цвет на неуказанный в списке __COLOR_VARIANTS
vehicle1.set_color('GREEN')

# Изменим цвет на разрешенный и поменяем владельца
vehicle1.set_color('White')
vehicle1.name_owner = 'Alex'

# Проверим изменения
vehicle1.print_info()