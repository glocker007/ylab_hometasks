import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vector.vector_3d import *
import pytest
#change to 3D
coords_1 = [1, 2., -1]
coords_2 = [-1., 2, 1]
coords_sub= [2, 0., -2]
coords_sum = [0, 4, 0]
coef_1 = 1.5
coords_mul_number = [1.5, 3, -1.5]
coords_mul_vectors = [-1, 4, -1]
dot_1_2 = [4, 0, 4] 
dot_2_1 = [-4, 0 , -4] 


@pytest.fixture()
def create_vector():
    return Vector3D(*coords_1), Vector3D(*coords_2) 

def test_setter():
    vec_1 = Vector3D(0,0,0)
    vec_1.x = 0.2
    assert(vec_1.x == 0.2)

def test_getter(create_vector):
    vec_1, _ = create_vector 
    assert vec_1.x == 1.
    assert vec_1.y == 2.
    assert vec_1.z == -1


def test_add(create_vector):
    vec_1, vec_2 = create_vector
    vec_sum = vec_1 + vec_2
    assert vec_sum == Vector3D(*coords_sum)

def test_sub(create_vector):
    vec_1, vec_2 = create_vector
    vec_sub = Vector3D(*coords_sub)
    assert vec_sub == Vector3D(*coords_sub)

def test_mul_number(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = vec_1 * coef_1
    assert vec_mul == Vector3D(*coords_mul_number)

def test_mul_vectors(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = vec_1 * vec_2
    assert vec_mul == Vector3D(*coords_mul_vectors)

def test_exception(create_vector):
    vec_1, _ = create_vector
    with pytest.raises(WrongArgumentType):
        tmp = vec_1 * "a"

def test_dot(create_vector):
    vec_1, vec_2 = create_vector
    dot_vec = vec_1.dot(vec_2)
    dot_vec_negative = vec_2.dot(vec_1)
    assert dot_vec == Vector3D(*dot_1_2)
    assert dot_vec_negative == Vector3D(*dot_2_1)

def test_right_mul(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = coef_1 * vec_1
    assert vec_mul == Vector3D(*coords_mul_number)

def test_creation():
    vec_1 = Vector2D(1, 2)
    vec_2 = Vector3D.create_vector_3D(vec_1, 2)
    vec_3 = Vector3D.create_vector_3D(vec_1, 1)
    vec_4 = Vector3D.create_vector_3D(vec_1, 0)
    vec_5 = Vector3D.create_vector(1, 2, 0)
    vec_6 = Vector3D.create_vector(0, 1, 2)
    vec_7 = Vector3D.create_vector(2, 0, 1)

    assert vec_2 == vec_5
    assert vec_3 == vec_7
    assert vec_4 == vec_6

def test_reduction():
    vec1 = Vector3D(1,2,3)
    assert Vector2D(1,2) == vec1.reduce_dim(2)
    assert Vector2D(2,3) == vec1.reduce_dim(0) 
    assert Vector2D(3,1) == vec1.reduce_dim(1)

def test_getitem():
    vec1 = Vector3D(1,2,3)
    assert vec1[0] == 1
    assert vec1[1] == 2
    assert vec1[2] == 3

def test_normalisation():
    vec1 = Vector3D(3,4,0)
    assert vec1.normalize().x == 3/5
    assert vec1.normalize().y == 4/5
