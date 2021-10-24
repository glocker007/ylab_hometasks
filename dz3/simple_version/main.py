"""import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""
from tkinter import *
import window.shapes_approxiamtions as sa
from vector.vector_3d import Vector3D, Vector2D
from math import pi

NUMBER_OF_FIGURES = 12

flat_figures = {0:"Circle", 1:"Square", 2:"Rectangle",
                3:"Trianlge", 4:"Trapezoid", 5:"Rhombus",
                6:"Sphere", 7:"Cube", 8:"Parallelepiped",
                9:"Pyramid", 10:"Cylinder", 11:"Cone"}

window  = Tk()
def draw_circle():
    print("Введите радиус")
    radius = float(input())
    root = Tk()
    circle = sa.Circle(radius, Vector3D(150,150,0)) 
    canvas = Canvas(root, width=300, height=300, bg='white')
    circle.draw(canvas)
    root.mainloop()
   
def draw_square():
    root = Tk()
    print("Введите длину стороны")
    side = float(input())
    square = sa.Square(side, Vector3D(150, 150,0))
    canvas = Canvas(root, width=300, height=300, bg='white')
    square.draw(canvas)
    root.mainloop()

def draw_rectangle():
    root = Tk()
    print("Через пробел введите длины сторон")
    sides = list(map(float, input().split()))
    rectangle = sa.Rectangle(sides[0], sides[1], Vector3D(150, 150,0))
    canvas = Canvas(root, width=300, height=300, bg='white')
    rectangle.draw(canvas)
    root.mainloop()

def draw_triangle():
    root = Tk()
    print("Введите 3 строки с 3мя числами через пробел- координаты вершин:")
    vertex = []
    for i in range(3):
        vertex.append(list(map(int, input().split())))
    lst = [Vector3D(*vertex[0]), Vector3D(*vertex[1]), 
            Vector3D(*vertex[2])]
    triangle = sa.Triangle(lst)
    canvas = Canvas(root, width=300, height=300, bg='white')
    triangle.draw(canvas)
    root.mainloop()

def draw_trapezoid():
    root = Tk()
    print("""Введите 4 длины сторон трапеции через пробел,
            чтобы 1ая и 3я были основаниями""")
    a,b,c,d = map(int, input().split())
    tr = sa.Trapezoid(Vector3D(250,250, 0), a, b, c, d)
    canvas = Canvas(root, width=500, height=500, bg='white')
    tr.draw(canvas)
    root.mainloop()

def draw_rhombus():
    root = Tk()
    print("""Введите сторонуромбаи угол между сторонами, через пробел (угол в радианах)""")
    side, angle = map(float, input().split())
    tr = sa.Parallelogramm(Vector3D(250,250, 0), side, side, angle)
    canvas = Canvas(root, width=500, height=500, bg='white')
    tr.draw(canvas)
    root.mainloop()

def draw_sphere():
    root = Tk()
    print("Введите радиус сферы")
    radius = int(input())
    sphere = sa.Sphere(radius, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    sphere.draw(canvas)
    root.mainloop()

def draw_cube():
    root = Tk()
    print("Введите сторону куба")
    side = int(input())
    cube = sa.Cube(side, Vector3D(250,250, 0))
    cube.rotate(Vector3D(1,1,0), pi/6)
    canvas = Canvas(root, width=500, height=500, bg='white')
    cube.draw(canvas)
    root.mainloop()


def draw_parallelepiped():
    root = Tk()
    print("Введите стороны параллелипипеда через пробел")
    a,b,c = map(int, input().split())
    parallelepiped = sa.Parallelepiped(a, b, c, Vector3D(250,250, 0))
    parallelepiped.rotate(Vector3D(1,1,0), pi/6)
    canvas = Canvas(root, width=500, height=500, bg='white')
    parallelepiped.draw(canvas)
    root.mainloop()

def draw_pyramid():
    root = Tk()
    print("Введите длину, ширину и высоту пирамиды через пробел")
    a, b, h = map(int, input().split())
    pyramid = sa.Pyramid(a, b, h, Vector3D(250,250, 0))
    pyramid.rotate(Vector3D(1,0,0), pi/2)
    pyramid.rotate(Vector3D(0,1,0), pi/3)
    pyramid.rotate(Vector3D(1,0,0), -pi/6)
    canvas = Canvas(root, width=500, height=500, bg='white')
    pyramid.draw(canvas)
    root.mainloop()

def draw_cylinder():
    root = Tk()
    print("Введите радиус и высоту через пробел")
    radius, height = map(int, input().split())
    cylinder = sa.Cylinder(radius, height, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    cylinder.rotate(Vector3D(1,0,0), pi/6)
    cylinder.draw(canvas)
    root.mainloop()

def draw_cone():
    root = Tk()
    print("Введите радиус и высоту через пробел")
    radius, height = map(int, input().split())
    cone = sa.Cone(radius, height, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    cone.rotate(Vector3D(1,0,0), pi/6)
    cone.draw(canvas)
    root.mainloop()


commands_onclick = {0: draw_circle, 1: draw_square, 2: draw_rectangle,
                    3: draw_triangle, 4: draw_trapezoid, 5: draw_rhombus,
                    6: draw_sphere, 7:draw_cube, 8:draw_parallelepiped,
                    9: draw_pyramid, 10:draw_cylinder, 11:draw_cone}


Frame(master=window, width=600, height=600, bg='white')
window.title("Choose an object")
buttons = []
for i in range(NUMBER_OF_FIGURES):
    buttons.append(Button(window,text = flat_figures[i], command=commands_onclick[i]))
    buttons[-1].grid(column=i//6, row=i % 6)
window.mainloop()

