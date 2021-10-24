import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vector.vector_2d import Vector2D, NotARightType
import pytest

coords_1 = [1, 2.]
coords_2 = [-1., 2]
coords_sub= [2, 0.]
coords_sum = [0, 4]
coef_1 = 1.5
coords_mul_number = [1.5, 3]
coords_mul_vectors = [-1, 4]
dot_1_2 = 4.
dot_2_1 = -4.


@pytest.fixture()
def create_vector():
    return Vector2D(*coords_1), Vector2D(*coords_2) 

def test_setter():
    vec_1 = Vector2D(0,0)
    vec_1.x = 0.2
    assert(vec_1.x == 0.2)

def test_getter(create_vector):
    vec_1, _ = create_vector 
    assert vec_1.x == 1.
    assert vec_1.y == 2.


def test_add(create_vector):
    vec_1, vec_2 = create_vector
    vec_sum = vec_1 + vec_2
    assert vec_sum == Vector2D(*coords_sum)

def test_sub(create_vector):
    vec_1, vec_2 = create_vector
    vec_sub = Vector2D(*coords_sub)
    assert vec_sub == Vector2D(*coords_sub)

def test_mul_number(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = vec_1 * coef_1
    assert vec_mul == Vector2D(*coords_mul_number)

def test_mul_vectors(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = vec_1 * vec_2
    assert vec_mul == Vector2D(*coords_mul_vectors)

def test_exception(create_vector):
    vec_1, _ = create_vector
    with pytest.raises(NotARightType):
        tmp = vec_1 * "a"

def test_dot(create_vector):
    vec_1, vec_2 = create_vector
    dot_vec = vec_1.dot(vec_2)
    dot_vec_negative = vec_2.dot(vec_1)
    assert dot_vec == dot_1_2
    assert dot_vec_negative == dot_2_1

def test_right_mul(create_vector):
    vec_1, vec_2 = create_vector
    vec_mul = coef_1 * vec_1
    assert vec_mul == Vector2D(*coords_mul_number)
