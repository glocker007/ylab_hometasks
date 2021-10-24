import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from shapes.shapes_2d import *


def test_square():
    square = Square(5)
    assert Square.number == 1
    assert Shape.number == 1

def test_area():
    square = Square(5)
    assert Square.number == 1
    assert square.area() == 25

def test_perimter():
    square = Square(5)
    assert square.perimeter() == 20

def test_rectangle_area():
    rec = Rectangle(5,6)
    assert Rectangle.number == 1
    assert rec.area() == 30

def test_rectangle_perimeter():
    rec = Rectangle(5,6)
    assert Rectangle.number == 1
    assert rec.perimeter() == 22 

def test_circle():
    circ = Circle(4)
    assert circ.area() == pi * 4 **2
    assert circ.perimeter() == 2 * pi * 4
    assert circ.radius == 4

def test_triangle():
    with pytest.raises(WrongArguments):
        Triangle(2,4,2)
    triangle = Triangle(3,4,5)
    assert triangle.area() == 3 * 4 * 0.5
    assert triangle.perimeter() == 12
    h = triangle.height()
    assert h[1] == 3 and h[0] == 4

def test_getter_triangle():
    a,b,c = Triangle(3,4,5).sides
    assert a == 3 and b == 4 and c == 5

def test_rectangle_getter():
    rec = Rectangle(2,5)
    a = rec.a_side
    b = rec.b_side
    assert a == 2 and b == 5
    
def test_triangle_setter():
    triangle = Triangle(3,4,5)
    triangle.sides = 2,3,4
    a,b,c = triangle.sides
    assert a == 2 and b == 3 and c == 4

def test_trapezoid():
    with pytest.raises(WrongArguments):
        Trapezoid(1,1,1,3)
    trapezoid = Trapezoid(2,5,10,5)
    assert trapezoid.area() == (3 * 4 * 0.5 + 3 * 4 * 0.5 + 2 * 3) 
    assert trapezoid.perimeter() == 22

def test_trapezoid_setter():
    trapezoid = Trapezoid(1,2,3,4)
    trapezoid.sides = 4,3,2,1
    assert trapezoid.sides == [4,3,2,1]

def test_parallelogramm():
    parallelogram = Parallelogramm(3,4, pi/2)
    assert parallelogram.area() == 12
    assert parallelogram.perimeter() == 14

def test_parallelogramm_setter():
    parallelogram = Parallelogramm(4, 5, pi/6)
    parallelogram.a_side = 2
    parallelogram.b_side = 3
    assert parallelogram.a_side == 2 and  parallelogram.b_side == 3

def test_rhombus():
    rhombus = Rhombus(4, pi/6)
    assert rhombus.area() == 4 * 4 * sin(pi/6)
    assert rhombus.perimeter() == 16

def test_rhombus_setter():
    rhombus = Rhombus(4, pi/6)
    rhombus.a_side = 3
    assert rhombus.b_side == 3
    assert rhombus.angle == pi/6
