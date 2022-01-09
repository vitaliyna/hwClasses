from abc import abstractmethod

class Point(object):
    "Класс точка"
    def __init__(self, x, y):
        self.koord1 = x
        self.koord2 = y 

class Line(object):                #в этом классе используется композиция с классом Point
   "Вычисляет длину отрезка по заданным координатам"
   def __init__(self, a, b, c, d):
       self.x1 = a
       self.y1 = b
       self.x2 = c
       self.y2 = d
       self.pointx = Point(self.x1, self.x2)
       self.pointy = Point(self.y1, self.y2)

   def length(self):
       return ((self.pointx.koord2 - self.pointx.koord1)**2 + (self.pointy.koord2 - self.pointy.koord1)**2)**.5

class Shape:                       #абстрактный класс
    def __init__(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

class Rect(Shape):
    "Класс наследуется от Shape и в композиции с Line"
    def __init__(self, length, a, b, c, d):
        super().__init__()
        self.length = length
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
        self.height = Line(self.x1, self.y1, self.x2, self.y2)

    def area(self):
        "вычисляет площадь прямоугольника"
        return self.length * self.height.length() 
    
    def perimeter(self):
        "вычисляет периметр прямоугольника"
        return (self.height.length() + self.length) * 2

class Square(Shape, Line):
    "Класс наследуется от Shape и Line"
    def __init__(self, a, b, c, d):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
        Shape.__init__(self)
        Line.__init__(self, self.x1, self.y1, self.x2, self.y2)
        self.__side = Line.length(self)

    def area(self):
        "вычисляет площадь квадрата"
        return self.__side**2

    def perimeter(self):
        "вычисляет периметр квадрата"
        return self.__side * 4

class Cube(Square):                #наследуется от Square
    def __init__(self, a, b, c, d):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
        Line.__init__(self, self.x1, self.y1, self.x2, self.y2)
        self.gran = Line.length(self)

    def volume(self):
        "вычисляет объем куба"
        return self.gran**3 

#инициализация отрезка
koordX1 = float(input("введите начальное значение координаты х на плоскости\n"))
koordX2 = float(input("введите конечное значение координаты х на плоскости\n"))
koordY1 = float(input("введите начальное значение координаты y на плоскости\n"))
koordY2 = float(input("введите конечное значение координаты y на плоскости\n"))

linija = Line(koordX1, koordY1, koordX2, koordY2)
print(f'Длина отрезка равна {linija.length()}')

#инициализация сторон прямоугольника и его вычисление
a = float(input("Введите длину прямоугольника. Его высотой будет длина отрезка, полученная ранее при расчете \n"))
rectSides = Rect(a, koordX1, koordY1, koordX2, koordY2)
print(f"Площадь Вашего прямоугольника равна {rectSides.area()}")
print(f"Периметр Вашего прямоугольника равен {rectSides.perimeter()}")

#инициализация стороы квадрата и его вычисление
s = Square(koordX1, koordY1, koordX2, koordY2)

print(f"Площадь вашего квадрата равна {s.area()}")
print(f"Периметр вашего квадрата равен {s.perimeter()}")

vCube = Cube(koordX1, koordY1, koordX2, koordY2)
print(f"Объем куба равен {vCube.volume()}")