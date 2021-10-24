from __future__ import annotations
from math import pi

class NotARightType(Exception):
    pass

class Vector2D:
    
    def __init__(self, x:float, y:float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __eq__(self, other: Vector2D) -> Vector2D:
        return self._x == other._x and self._y == other._y

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self._x - other._x, self._y - other._y) 

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self._x + other._x, self._y + other._y)
    
    def multiplication(self, other: 'Vector2D, float') -> Vector2D:
        if isinstance(other, float):
            return Vector2D(self._x * other, self._y * other)
        elif type(self) == type(other):
            return Vector2D(self._x * other._x, self._y * other._y)
        else:
            raise NotARightType
        
    def __mul__(self, other:'Vector2D, float') -> Vector2D:
        return self.multiplication(other)

    def dot(self, other: 'Vector2D') -> float:
        return self._x * other._y - self._y * other._x

    __rmul__ = __mul__

    def length(self) -> float:
        return (self._x**2 +  self._y**2) ** 0.5
