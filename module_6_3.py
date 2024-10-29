class Horse:
    """Объвим класс Лошадь в качестве аргументов принимает
    начальную позицию - xdistance и звук - sound"""

    def __init__(self, xdistance=0, sound='Frr'):
        # При инициализации установим аргументы
        self.xdistance = xdistance
        self.sound = sound

    # Функция изменения позиции при беге Лошади
    def run(self, dx):
        self.xdistance = self.xdistance + dx


"""Объвим класс Орел в качестве аргументов принимает 
  начальную позицию - ydistance и звук - sound"""


class Eagle:

    def __init__(self, ydistance=0, sound='I train, eat, sleep and repeat'):
        # При инициализации установим аргументы
        self.ydistance = ydistance
        self.sound = sound

    # Функция изменения позиции при полете Орла
    def fly(self, dy):
        self.ydistance = self.ydistance + dy


class Pegasus(Horse, Eagle):
    """Класс Пегас наследует аргументы и методы классов в последовательности:
    1. Класс Horse
    2. Класс Eagle"""

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    # Функция отслеживания перемещения Пегаса
    def move(self, dx, dy):
        # Использование функции полета Орла
        self.fly(dy)
        # Использование функции бега Лошади
        self.run(dx)

    # Определение текущей позиции Пегаса исходя из бега и полета
    def get_pos(self):
        return (self.xdistance, self.ydistance)

    # Функция голоса
    def voice(self):
        print(self.sound)


# Создадим экземпляр класса Пегас
p1 = Pegasus()

# Выведем текущую позицию Пегаса
print(p1.get_pos())

# Изменим позицию Пегаса
p1.move(10, 15)
# Выведем текущую позицию Пегаса
print(p1.get_pos())

# Изменим позицию Пегаса
p1.move(-5, 20)
# Выведем текущую позицию Пегаса
print(p1.get_pos())

# Опробуем голос Пегаса
p1.voice()