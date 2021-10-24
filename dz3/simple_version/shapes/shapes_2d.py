from __future__ import annotations
from math import pi, sin, cos
class WrongArguments(Exception):
    pass

class Shape:
    number = 0
    def __init__(self):
        Shape.add()

    def area(self):
        pass

    def perimeter(self):
        pass

    @classmethod
    def add(cls):
        cls.number += 1

    @classmethod
    def dec(cls):
        cls.number -= 1

    def __del__(self):
        Shape.dec()

class Square(Shape):
    number = 0

    def __init__(self, x_: float):
        super().__init__()
        self._x = x_
        Square.add()

    @property
    def a_side(self) -> float:
        return self._x

    @a_side.setter
    def a_side(self, value: float):
        self._x = value

    def area(self) -> float:
        return self._x ** 2

    def perimeter(self) -> float:
        return self._x * 4

    def __del__(self):
        Square.dec()


class Rectangle(Square):
    number = 0
    """takes two argiuments - sides of Rectangle
       added new argument _y"""
    def __init__(self, x_:float, y_:float):
        super().__init__(x_)
        self._y = y_
        Rectangle.add()

    @property
    def b_side(self) -> float:
        return self._y

    @b_side.setter
    def b_side(self, key:float):
        self._y = key

    def area(self) -> float:
        return self._x * self._y

    def perimeter(self) -> float:
        return 2 * (self._y + self._x)

    def __del__(self):
        Rectangle.dec()


class Circle(Shape):
    number = 0

    def __init__(self, r_:float):
        super().__init__()
        self._r = r_
        Circle.add()

    @property
    def radius(self) ->float:
        return self._r

    @radius.setter
    def radius(self, key:float):
        self._r = key

    def area(self) -> float:
        return pi * self._r ** 2

    def perimeter(self) -> float:
        return 2 * pi * self._r

    def __del__(self):
        Circle.dec()


class Triangle(Shape):

    number = 0

    """Takes three sides as input,
    checks is it possible to construct a triangle"""
    def __init__(self, *args : 'list[float]'):
        if ((args[0] + args[1]  <= args[2])
        or (args[1] + args[2] <= args[0])
        or (args[0] + args[2] <= args[1])):
            raise WrongArguments
        super().__init__()
        self._sides = [*args]
        Triangle.add()

    @property
    def sides(self) -> 'list[float]':
        return self._sides

    def height(self) -> 'list[float]':
        area = self.area()
        height = [0, 0, 0]
        for i in range(3):
            height[i] = area / self._sides[i] * 2
        return height

    @sides.setter
    def sides(self, key: 'list[float]'):
        for i in range(3):
            self._sides[i] = key[i]

    def perimeter(self) -> float:
        return sum(self._sides)

    def area(self) -> float:
        p_half = self.perimeter()/2
        product = 1
        for i in range(3):
            product *= (p_half - self._sides[i])
        area = (p_half * product) ** 0.5
        return area

    def __del__(self):
        Triangle.dec()

"""the most undetermined class, because of restrictions like parallel lines"""
class Trapezoid(Shape):
    number = 0

    """bases are 1't and 3'd. Takes list of numbers as input, consideder
    that bases are first and third sides and checks if trapezoid is possible to
    contruct for this lengths """
    def __init__(self, *args: float):
        super().__init__()
        lists = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 3, 1], [2, 3, 1, 0]]
        for lst in lists:
            sum_ = 0
            for elem in lst[0:3]:
                sum_ += args[elem]
            if sum_ <= args[lst[3]]:
                raise WrongArguments
        self._sides = [*args]
        Trapezoid.add()

    """its not inherited from trianlge so should have it's own getter"""
    @property
    def sides(self) -> float:
        return self._sides

    @sides.setter
    def sides(self, key):
        for i in range(4):
            self._sides[i] = key[i]

    """area is shattered on two parts , one - triangle ,
    other is parralelogram - but we don't use it's(parralelogram's)
    methods to calculate it's area , we are use height and the minimum base
    """
    def area(self) -> float:
        triangle = Triangle(self._sides[1], self._sides[3],
                            abs(self._sides[2] - self._sides[0]))
        _, _, height = triangle.height()
        return triangle.area() + height * min(self._sides[2],self._sides[0])

    def perimeter(self) -> float:
        return sum(self._sides)

    def __del__(self):
        Trapezoid.dec()


class Parallelogramm(Rectangle):
    number = 0


    """Inherited from Shape, has two sides, and angle between them"""
    def __init__(self, x_:float, y_:float, angle:float):
        super().__init__(x_,y_)
        self._angle = angle
        Parallelogramm.add()

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle:float):
        self._angle = angle

    def area(self) -> float:
        return self._x * self._y * sin(self._angle)

    """length of parallelogramm,
    we actually don't need this one """
    def perimeter(self) -> float:
        return 2 * (self._x + self._y)

    def __del__(self):
        Parallelogramm.dec()


class Rhombus(Parallelogramm):

    number = 0

    """ rhombus takes two arguments first - length of sides,
    second - angle between them. Despite of less arguments
    this class inherit parallelogramm, just properly managing second
    side """

    def __init__(self, side: float, radian:float):
        super().__init__(side, side, radian)
        Rhombus.add()


    @property
    def a_side(self) -> float:
        return self._x

    @a_side.setter
    def a_side(self, x_:float):
        self._x = x_
        self._y = x_

    def __del__(self):
        Rhombus.dec()
