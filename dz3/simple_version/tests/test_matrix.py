import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from vector.transformation import *

matrix = [[0,1,0],[1,0,0],[0,0,1]]

vector = Vector3D(1,2,3)
@pytest.fixture
def get_matrix():
    return Matrix(matrix)

def test_matrix_dot(get_matrix):
    mat = get_matrix
    v_test = mat.dot(vector)
    assert v_test.x == 2
    assert v_test.y == 1
    assert v_test.z == 3

def test_matrix_getitem(get_matrix):
    mat = get_matrix
    assert mat[0][1] == 1
    assert mat[1][0] == 1

def test_matrix_rotation(get_matrix):
    vec = Vector3D(0,1,0)
    vec_rot = Vector3D(0,0,1)
    expected = Vector3D(-1,0,0)
    lst = [vec]
    result = Matrix.rotation_around_vector(vec_rot, pi/2, Vector3D(0,0,0), lst)
    print(result[0].x, result[0].y, result[0].z)
    assert result[0].x == expected.x
    assert result[0].z == expected.z
