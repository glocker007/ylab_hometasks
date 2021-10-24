from __future__ import annotations
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shapes.shapes_2d import *

class Shape3d(Shape):
    number = 0
    def volume(self):
        pass


class Sphere(Circle, Shape3d):
    number = 0

    def __init__(self, radius: float):
        Circle.__init__(self, radius)
        Shape3d.__init__(self)
        Sphere.add()

    def volume(self) -> float:
        return pi * self._r ** 3 /3

    def area(self) -> float:
        return 4 * Circle.area(self)

    def __del__(self):
        Sphere.dec()


class Cube(Square, Shape3d):
    number = 0

    def __init__(self, side: float):
        Square.__init__(self, side)
        Shape3d.__init__(self)
        Cube.add()

    def volume(self) -> float:
        return self._x ** 3

    def perimeter(self) -> float:
        return self._x * 12

    def area(self) -> float:
        return 6 * Square.area(self)

    def __del__(self):
        Sphere.dec()


class Parallelepiped(Rectangle, Shape3d):
    number = 0

    def __init__(self, side_1: float, side_2: float, side_3:float):
        Rectangle.__init__(self, side_1, side_2)
        Shape3d.__init__(self)
        self._side_3 = side_3
        Parallelepiped.add()

    @property
    def c_side(self) -> float:
        return self._side_3

    @c_side.setter
    def c_side(self, key: float):
        self._side_3 = key

    def area(self) -> float:
        return 2 * (self.a_side * self.b_side +
                self.a_side * self.c_side + self.b_side * self.c_side)

    def volume(self) -> float:
        return Rectangle.area(self) * self.c_side

    def perimeter(self) -> float:
        return 2 * (self.a_side + self.b_side + self.c_side)

    def __del__(self):
        Parallelepiped.dec()


class Pyramid(Rectangle, Shape3d):
    number = 0
    """considered that it's  regular quadrangular pyramid for simplicity"""
    def __init__(self, side_base_1: float, side_base_2: float, height: float):
        Rectangle.__init__(self, side_base_1, side_base_2)
        Shape3d.__init__(self)
        self._height = height
        Pyramid.add()

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height:float):
        self._height = height

    def area(self) -> float:
        ref_1 = (self.height**2 + (self.a_side/2) ** 2) ** 0.5 /\
            (self.a_side / 2)
        ref_2 = (self.height**2 + (self.b_side/2) ** 2) ** 0.5 /\
            (self.b_side / 2)
        area_half = Rectangle.area(self)/2
        area_sum = area_half * (ref_1 + ref_2 + 2)
        return area_sum

    def volume(self):
        return self.height * Rectangle.area(self) / 3

    def perimeter(self):
        base_diag_half = (self.a_side**2 + self.b_side**2) ** 0.5 / 2
        side = (base_diag_half ** 2 + self.height ** 2) ** 0.5
        return 4 * side + Rectangle.perimeter(self)

    def __del__(self):
        Pyramid.dec()


class Cylinder(Circle, Shape3d):

    number = 0

    """regular cylinder, doesn't have perimeter
    so this method inherited from Circle"""
    def __init__(self, radius:float, height: float):
        Circle.__init__(self, radius)
        Shape3d.__init__(self)
        self._height = height
        Cylinder.add()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, key:float):
        self._height = key

    def area(self) -> float:
        return 2 * (pi * self.radius * self.height + Circle.area(self))

    def volume(self) -> float:
        return Circle.area(self) * self.height

    def __del__(self):
        Cylinder.dec()


class Cone(Circle, Shape3d):

    number = 0
    """Didn't inherited from Cylinder, and reused same methods,
    because its similar objects with different properties,
    it's not inheried from cylinder"""
    def __init__(self, radius:float, height:float):
        Circle.__init__(self, radius)
        Shape3d.__init__(self)
        self._height = height
        Cone.add()

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, key: float):
        self._height = key 

    def area(self) -> float:
        side = (self.radius ** 2 + self.height ** 2) ** 0.5
        return pi * self.radius * (side + self.radius)

    def volume(self) -> float:
        return self.height * Circle.area(self) / 3

    def __del__(self):
        Cone.dec()
