from __future__ import annotations
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vector.vector_3d import Vector3D
from math import pi, cos, sin

class Matrix:

    def __init__(self, matrix: 'list[list[float]]'):
        self._matrix = matrix
    
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, key:'list[list[float]]'):
        self._matrix = key
    
    def __getitem__(self, key: 'int'):
        return self._matrix[key]

    def dot(self, other: 'Vector3D') -> 'Vector3D':
        if isinstance(other, Vector3D):
            tmp_vec = Vector3D(0,0,0)
            for i in range(3):
                for j in range(3):
                    tmp_vec[i] += other[j] * self.matrix[i][j]
            return tmp_vec
        else:
            raise WrongArgumentType

    @staticmethod
    def rotation_around_vector(vector:'Vector3D', angle: float, 
            center: 'Vector3D', vectors_list: 'list[Vector3D]'):
        tmp_list = []
        matrix = Matrix.rotation_matrix(vector, angle) 
        for v in vectors_list:
            tmp_list.append(matrix.dot(v - center) + center)
        return tmp_list

    @classmethod
    def rotation_matrix(cls, vector: 'Vector3D', angle:float) -> 'Matrix':
        norm_vector = vector.normalize()
        x = norm_vector.x
        y = norm_vector.y
        z = norm_vector.z
        matrix = [[cos(angle) + (1 - cos(angle))*x**2,
                    (1 - cos(angle))*x*y - sin(angle)*z,
                    (1 - cos(angle))*x*z + sin(angle)*y],
                  [(1 - cos(angle))*y*x + sin(angle)*z,
                    cos(angle) + (1 - cos(angle))*y**2,
                    (1 - cos(angle))*y*z - sin(angle)*x],
                  [(1 - cos(angle))*z*x - sin(angle)*y,
                    (1 - cos(angle))*z*y + sin(angle)*x,
                    cos(angle) + (1 - cos(angle)) * z**2]]
        return cls(matrix)
