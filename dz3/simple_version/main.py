"""import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""
from tkinter import * 
import window.shapes_approxiamtions as sa
from vector.vector_3d import Vector3D, Vector2D
from math import pi
import time
NUMBER_OF_FIGURES = 12

flat_figures = {0:"Circle", 1:"Square", 2:"Rectangle",
                3:"Triangle", 4:"Trapezoid", 5:"Rhombus", 6:"Sphere", 7:"Cube", 8:"Parallelepiped",
                9:"Pyramid", 10:"Cylinder", 11:"Cone"}


def rotate_func(master:'Frame', canvas:'Canvas', shape:'shapes.*', key:'string'):
    key_rotation = {'<Right>': (Vector3D(0,1,0), pi/12),
            '<Left>' : (Vector3D(0,1,0), -pi/12),
            '<Down>' : (Vector3D(1,0,0), -pi/12),
            '<Up>' : (Vector3D(1,0,0), pi/12)
            }
    def Handler(event):
        shape.rotate(*key_rotation[key])
        canvas.delete("all")
        shape.draw(canvas)
        master.update()
    return Handler

def bind_buttons(master:'Frame', canvas:'Canvas', shape:'shapes.*'):
    keys = ['<Right>', '<Left>', '<Down>', '<Up>'] 
    for key in keys:
        master.bind(key, rotate_func(master, canvas, shape, key))


def draw_circle(list_arguments):
    radius = list_arguments[0]
    root = Tk()
    circle = sa.Circle(radius, Vector3D(150,150,0)) 
    canvas = Canvas(root, width=300, height=300, bg='white')
    circle.draw(canvas)
    bind_buttons(root, canvas, circle)
    root.mainloop()
   
def draw_square(list_arguments):
    side = list_arguments[0]
    root = Tk()
    square = sa.Square(side, Vector3D(150, 150,0))
    canvas = Canvas(root, width=300, height=300, bg='white')
    square.draw(canvas)
    bind_buttons(root, canvas, square)
    root.mainloop()

def draw_rectangle(sides:'list[int]'):
    root = Tk()
    rectangle = sa.Rectangle(sides[0], sides[1], Vector3D(150, 150,0))
    canvas = Canvas(root, width=300, height=300, bg='white')
    rectangle.draw(canvas)
    bind_buttons(root, canvas, rectangle)
    root.mainloop()

def draw_triangle(list_arguments):
    vertex = [[],[],[]]
    idx = 0

    for i in range(3):
        for j in range(3):
            vertex[i].append(list_arguments[idx])
            idx += 1

    root = Tk()
    lst = [Vector3D(*vertex[0]), Vector3D(*vertex[1]), 
            Vector3D(*vertex[2])]
    triangle = sa.Triangle(lst)
    canvas = Canvas(root, width=300, height=300, bg='white')
    triangle.draw(canvas)
    bind_buttons(root, canvas, triangle)
    root.mainloop()

def draw_trapezoid(list_arguments):
    root = Tk()
    a_side, b_side, c_side, d_side = list_arguments
    tr = sa.Trapezoid(Vector3D(250,250, 0), a_side, b_side, c_side, d_side)
    canvas = Canvas(root, width=500, height=500, bg='white')
    tr.draw(canvas)
    bind_buttons(root, canvas, tr)
    root.mainloop()

def draw_rhombus(list_arguments):
    root = Tk()
    side, angle = list_arguments
    tr = sa.Parallelogramm(Vector3D(250,250, 0), side, side, angle)
    canvas = Canvas(root, width=500, height=500, bg='white')
    tr.draw(canvas)
    bind_buttons(root, canvas, tr)
    root.mainloop()

def draw_sphere(list_arguments):
    root = Tk()
    radius = list_arguments[0]
    sphere = sa.Sphere(radius, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    sphere.draw(canvas)
    bind_buttons(root, canvas, sphere)
    root.mainloop()

def draw_cube(list_arguments):
    root = Tk()
    side = list_arguments[0]
    cube = sa.Cube(side, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    cube.draw(canvas)
    bind_buttons(root, canvas, cube)
    root.mainloop()


def draw_parallelepiped(list_arguments):
    root = Tk()
    a_side, b_side, c_side = list_arguments
    parallelepiped = sa.Parallelepiped(a_side, b_side, c_side, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    parallelepiped.draw(canvas)
    bind_buttons(root, canvas, parallelepiped)
    root.mainloop()

def draw_pyramid(list_arguments):
    root = Tk()
    a_side, b_side, h = list_arguments
    pyramid = sa.Pyramid(a_side, b_side, h, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    pyramid.draw(canvas)
    bind_buttons(root, canvas, pyramid)
    root.mainloop()

def draw_cylinder(list_arguments):
    root = Tk()
    radius, h = list_arguments
    cylinder = sa.Cylinder(radius, h, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    cylinder.draw(canvas)
    bind_buttons(root, canvas, cylinder)
    root.mainloop()

def draw_cone(list_arguments):
    root = Tk()
    radius, h = list_arguments
    cone = sa.Cone(radius, h, Vector3D(250,250, 0))
    canvas = Canvas(root, width=500, height=500, bg='white')
    cone.draw(canvas)
    bind_buttons(root, canvas, cone)
    root.mainloop()


commands_onclick = {0: draw_circle, 1: draw_square, 2: draw_rectangle,
                    3: draw_triangle, 4: draw_trapezoid, 5: draw_rhombus,
                    6: draw_sphere, 7:draw_cube, 8:draw_parallelepiped,
                    9: draw_pyramid, 10:draw_cylinder, 11:draw_cone}


def Requesthandler(index: int, entries: 'list[Entry]'):
    def Handler():
        args = []
        try:
            for entry in entries:
                information = entry.get()
                for string in information.split():
                    args.append(float(string))
        except Exception:
            print("wrond arguemnts")
            return CommandRequest(index) 
        commands_onclick[index](args)
    return Handler

number_of_event = {
        "Circle": (1, ["Введите радиус"]),
        "Square": (1, ["Введите длину стороны"]),
        "Rectangle": (2,["Введите длину стороны","Введите длину стороны"]),
        "Trapezoid": (4,["Введите длину Основания", "Введите длинy стороны",
            "Введите длину Основания", "Введите длину стороны"]),
        "Rhombus": (2, ["Введите длину стороны", "Введите угол в радианах"]),
        "Triangle": (3, ["Введите координаты вешин через пробел"
            for i in range(3)]),
        "Sphere" : (1, ["Введите радиус"]),
        "Cube" : (1, ["Введите длину стороны"]),
        "Parallelepiped":(1, ["Введите длины трех сторон через пробел"]),
        "Cylinder" : (1, ["Введите радиус и высоту через пробел"]),
        "Cone" : (1, ["Введите радиус и высоту через пробел"]),
        "Pyramid" : (3, ["Введите длину стороны" for i in range(2)] + 
            ["Введите высоту"])
        }

    

def CommandRequest(index: int):
    def Handler():
        wd = Tk()
        wd.geometry("600x150")
        figure = flat_figures[index]
        number_of_tabs, strings = number_of_event[figure]
        entries = []
        labels = []
        for i in range(number_of_tabs):
            labels.append(Label(wd, text = strings[i]))
            labels[-1].grid(column= 0, row = i)
            entries.append(Entry(wd))
            entries[-1].grid(column = 1, row = i)
        button = Button(wd, text = "Set", command = Requesthandler(index, entries))
        button.grid(column = 0, row = number_of_tabs + 1)
        wd.mainloop()

    return Handler


window  = Tk()
Frame(master=window, width=600, height=600, bg='white')
window.title("Choose an object")
buttons = []
for i in range(NUMBER_OF_FIGURES):
    buttons.append(Button(window,text = flat_figures[i], command = CommandRequest(i)))
    buttons[-1].grid(column=i//6, row=i % 6)
window.mainloop()

