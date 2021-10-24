import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shapes.shapes_3d import *
import pytest

def test_sphere():
    sphere = Sphere(3)
    assert sphere.radius == 3
    assert sphere.area() == 4 * pi * 3**2
    assert sphere.perimeter() == 3 * 2 * pi
    assert sphere.volume() == pi * 3 ** 3 /3

def test_sphere_getter_setter():
    sphere = Sphere(3)
    sphere.radius = 4
    assert sphere.radius == 4
    assert sphere.area() == 4 * pi * 4 ** 2

def test_cube():
    cube = Cube(3)
    assert cube.a_side == 3
    assert cube.volume() == 3 ** 3
    assert cube.area() == 3 ** 2 * 6
    assert cube.perimeter() == 3 * 12

def test_parallelepiped():
    parallelepiped = Parallelepiped(1, 2, 3)
    assert parallelepiped.a_side == 1
    assert parallelepiped.b_side == 2
    assert parallelepiped.c_side == 3
    assert parallelepiped.area() == 22
    assert parallelepiped.perimeter() == 12
    assert parallelepiped.volume() == 6

def test_pyramid():
    pyramid = Pyramid(8, 8, 3)
    expected = 8 * 8 * (5/4 + 1)
    side = ((2 * 4**2) + 3 ** 2) ** 0.5 
    assert pyramid.area() == expected
    assert pyramid.perimeter() == 4 * side + 8 * 4
    assert pyramid.volume() == 8 * 8 * 3 /3
    assert pyramid.height == 3
    assert pyramid.a_side == 8
    assert pyramid.b_side == 8

def test_cylinder():
    cylinder = Cylinder(3, 4)
    assert cylinder.radius == 3
    assert cylinder.area() == 2 * 3**2 * pi + 2 * pi * 3 * 4
    assert cylinder.volume() == 3 ** 2 * pi * 4
    assert cylinder.radius == 3
    assert cylinder.height == 4
