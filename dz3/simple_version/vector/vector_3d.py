from __future__ import annotations
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vector.vector_2d import *
from math import pi

class WrongArgumentType(Exception):
    pass


class Vector3D:

    def __init__(self, x_coord: float, y_coord: float, z_coord: float):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord
    
    def __eq__(self, other: 'Vector3D') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: 'Vector3D'):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other: 'Vector3D'):
        if isinstance(other, Vector3D):
            return Vector3D(self.x*other.x,
                            self.y*other.y,
                            self.z*other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise WrongArgumentType

    __rmul__ = __mul__

    def __truediv__(self, other:float) -> 'Vector3D':
        return Vector3D(self.x/other, self.y/other, self.z/other)

    def __getitem__(self, key: int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise WrongArgumentType
    
    def __setitem__(self, key: int, value: float):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise WrongArgumentType

    def dot(self, other: 'Vector3D'):
        if isinstance(other, Vector3D):
            return Vector3D(self.y * other.z - self.z * other.y,
                            self.z * other.x - self.x * other.z,
                            self.x * other.y - self.y * other.x)
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def normalize(self):
        return self / self.length()

    @classmethod
    def create_vector_3D(cls, vector: 'Vector2D',
                         axis: '0, 1, 2') -> 'Vector3D':
        if axis == 0:
            return cls(0, vector.x, vector.y)
        if axis == 1:
            return cls(vector.y, 0, vector.x)
        if axis == 2:
            return cls(vector.x, vector.y, 0)
        raise WrongArgumentType
    
    @classmethod
    def create_vector(cls, x:float, y: float, z:float) -> 'Vector3D':
        return cls(x,y,z)

    def reduce_dim(self, axis: '0, 1, 2') -> 'Vector2D':
        if axis == 0:
            return Vector2D(self.y, self.z)
        if axis == 1:
            return Vector2D(self.z, self.x)
        if axis == 2:
            return Vector2D(self.x, self.y)
