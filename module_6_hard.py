from math import pi

# Создадим основной класс
class Figure:
  __sides = []
  __color = []
  filled =False

  sides_count = 0
# Инициация объектов
  def __init__(self, rgb, *side):
    self.color = list(rgb)
    self.side = side[0]
    self.filled = True

# Взять цвет
  def get_color(self):
    self.__color = self.color
    self.filled = True
    return self.__color

# Проверка валидности цвета
  def _is_valid_color(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b
    if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
      return True
    else:
      return False

# Установка цвета
  def set_color(self, r, g, b):
    if self._is_valid_color(r, g, b):
      self.color = [self.r, self.g, self.b]

# Проверка валибности сторон
  def __is_valid_sides(self, *args):
    #for side in self.sides:
     if len(self.sides) == 1:
       return True
     else:
       return False

# Взять стороны
  def get_sides(self):
    self.__sides = [self.side] * self.sides_count
    return self.__sides

# Расчет периметра
  def __len__(self, *args):
    return self.side * self.sides_count

# Установка сторон
  def set_sides(self, *args):
    self.sides = list(args)
    if self.__is_valid_sides(self, *args):
      self.side = self.sides[0] * self.sides_count
      self.get_sides()
    else:
      return False
      #self.sides = [1] * self.sides_count
      #self.get_sides()

# Дочерний класс Круга
class Circle(Figure):
  sides_count = 1
  def get_square(self):
    return (self.side ** 2) / (4 * pi)

# Дочерний класс Треугольника
class Triangle(Figure):
  sides_count = 3
  def get_square(self):
      return (self.side ** 2) * ((self.sides_count) ** 0.5) / 4

# Дочерний класс Куба
class Cube(Figure):
  sides_count = 12
  def get_volume(self):
      return self.side ** 3

# Создание экземпляров
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 100), 10)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра куба:
print(cube1.__len__())

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади круга
print(circle1.get_square())

# Проверка площади треугольника
print(triangle1.get_square())

# Проверка периметра круга
print(circle1.__len__())

# Проверка периметра треугольника
print(triangle1.__len__())
