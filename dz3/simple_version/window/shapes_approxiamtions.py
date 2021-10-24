import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import shapes.shapes_3d as shapes
import vector.vector_3d as vector
from tkinter import *
from math import pi, sin, cos
import vector.transformation as transform


class VectorChain:

    def __init__(self, lst: 'list[Vector3D]'):
        self._chain = lst

    def __getitem__(self, key: 'int') -> 'vector.Vector3D':
        return self._chain[key]

    def draw(self, canvas:'Canvas'):
        for i in range(len(self._chain)):
            canvas.create_line(self._chain[i].x, 
                                self._chain[i].y,
                                self._chain[(i+1)%len(self)].x,
                                self._chain[(i+1)%len(self)].y)
        canvas.pack()

    def rotate(self, angle:float, vector_rot: 'vector.Vector3D',
            center: 'vector.Vector3D'):
        self._chain = transform.Matrix.rotation_around_vector(vector_rot, 
                angle, center, self._chain)
        return self

    def create_rotation(self, angle:float, vector_rot: 'vector.Vector3D',
            center: 'vector.Vector3D'):
        chain = transform.Matrix.rotation_around_vector(vector_rot, 
                angle, center, self._chain)
        return VectorChain(chain)

    def __len__(self):
        return len(self._chain)


class Circle(shapes.Circle):

    def __init__(self, radius:float, center: 'vector.Vector3D'):
        shapes.Circle.__init__(self, radius)
        self._center = center
        self._chain = self.create_vector_chain(50, 0, vector.Vector3D(0,1,0))

    def create_vector_chain(self, detalization: int,
            rotate: float, vec: 'Vector3D'):
        lst = []
        angle = 2 * pi / detalization
        sum_angle = 0
        for i in range(detalization):
            lst.append(self._center + vector.Vector3D(self.radius * cos(sum_angle),
                self.radius * sin(sum_angle), 0))
            sum_angle += angle
        return VectorChain(lst).rotate(rotate, vec, self._center)

    def rotate(self, vector_rot:'Vector3D', angle:float):
        self._chain = self._chain.rotate(angle, vector_rot, self._center)

    def draw(self, canvas:'Canvas'):
        self._chain.draw(canvas)


class Square(shapes.Square):

    def __init__(self, a_side: float, center: 'vector.Vector3D'):
        shapes.Square.__init__(self, a_side)
        self._center = center
        self._chain = self.create_vector_chain(0, vector.Vector3D(0,1,0))

    def create_vector_chain(self, rotate: float, vec: 'vector.Vector3D'):
        lst = []
        zip_1 = [1, 1, -1, -1]
        zip_2 = [1, -1, -1, 1]
        for i,j in zip(zip_1, zip_2):
               lst.append(self._center + vector.Vector3D(i*self.a_side/2, j*self.a_side/2, 0)) 
        return VectorChain(lst)
    
    def rotate(self, vector_rot:'vector.Vector3D', angle:float):
        self._chain = self._chain.rotate(angle, vector_rot, self._center)

    def draw(self, canvas:'Canvas'):
        self._chain.draw(canvas)


class Rectangle(Square, shapes.Rectangle):
    
    def __init__(self, a_side:float, b_side:float,center:'vector.Vector3D'):
        shapes.Rectangle.__init__(self, a_side, b_side)
        self._center = center
        self._chain = self.create_vector_chain(0, vector.Vector3D(0,1,0))
    
    def create_vector_chain(self, rotate:float, vec:'vector.Vector3D'):
        lst = []
        zip_1 = [1, 1, -1, -1]
        zip_2 = [1, -1, -1, 1]
        for i,j in zip(zip_1, zip_2):
            lst.append(self._center + vector.Vector3D(i*self.a_side/2, j*self.b_side/2, 0))
        return VectorChain(lst)


class Triangle(shapes.Triangle, VectorChain):
    
    def __init__(self, lst:'list[vector.Vector3D]'):
        VectorChain.__init__(self, lst)
        self._center = vector.Vector3D(0,0,0)
        for i in range(len(self._chain)):
            self._center += self._chain[i]/3
        lengths = []
        for i in range(3):
            lengths.append((self._chain[i] - self._chain[(i+1) % 3]).length())
        shapes.Triangle.__init__(self, *lengths)


class Trapezoid(shapes.Trapezoid):
    
    def __init__(self,center:'vector.Vector3D', *sides):
        shapes.Trapezoid.__init__(self, *sides)
        self._center = center
        self._chain = self.create_vector_chain(0, vector.Vector3D(0,0,0))
    
    def create_vector_chain(self, rotate:float, vec:'vector.Vector3D'):
        triangle = shapes.Triangle(self.sides[1], self.sides[3],
                abs(self.sides[0] - self.sides[2]))
        _,_,height = triangle.height()
        cos_1 = (1 - (height/self.sides[1])**2)**0.5
        cos_2 = (1 - (height/self.sides[3])**2)**0.5
        lst = []
        lst.append(vector.Vector3D(0,0,0))
        lst.append(vector.Vector3D(self.sides[1] * cos_1, height, 0))
        lst.append(vector.Vector3D(max(self.sides[0], self.sides[2]) -
            self.sides[3]*cos_2, height, 0))
        lst.append(vector.Vector3D(max(self.sides[0], self.sides[2]), 0, 0))
        local_center = vector.Vector3D(0,0,0)
        for i in range(len(lst)):
            local_center += lst[i]/4
        shift = self._center - local_center
        for i in range(len(lst)):
            lst[i] += shift
        return VectorChain(lst)

    def rotate(self, vector_rot:'vector.Vector3D', angle:float):
        self._chain = self._chain.rotate(angle, vector_rot, self._center)

    def draw(self, canvas:'Canvas'):
        self._chain.draw(canvas)


class Parallelogramm(shapes.Parallelogramm):
    
    def __init__(self, center:'vector.Vector3D',
            side_a:float, side_b:float, angle:float):
        shapes.Parallelogramm.__init__(self, side_a, side_b, angle)
        self._center = center
        self._chain = self.create_vector_chain(0, vector.Vector3D(0,0,0))

    def create_vector_chain(self, rotate:float, vec:'vector.Vector3D'):
        lst = []
        lst.append(vector.Vector3D(0,0,0))
        lst.append(vector.Vector3D(self.a_side * cos(self.angle),
            self.a_side * sin(self.angle),0))
        lst.append(vector.Vector3D(self.a_side * cos(self.angle) + self.b_side,
            self.a_side * sin(self.angle), 0))
        lst.append(vector.Vector3D(self.b_side, 0, 0))
        local_center = vector.Vector3D(0,0,0)
        for i in range(len(lst)):
            local_center += lst[i]/4
        shift = self._center - local_center
        for i in range(len(lst)):
            lst[i] += shift
        return VectorChain(lst)

    def rotate(self, vector_rot:'vector.Vector3D', angle:float):
        self._chain = self._chain.rotate(angle, vector_rot, self._center)

    def draw(self, canvas:'Canvas'):
        self._chain.draw(canvas)


class Sphere(shapes.Sphere):

    def __init__(self, radius: float, center: 'vector.Vector3D'):
        shapes.Sphere.__init__(self, radius)
        self._center = center
        self._chain = self.create_vector_chain(50)

    def create_vector_chain(self, detalization:int):
        lst = []
        angle = 2 * pi/detalization
        sum_angle = 0
        for i in range(detalization):
            lst.append(self._center + vector.Vector3D(self.radius * cos(sum_angle),
                self.radius * sin(sum_angle), 0))
            sum_angle += angle
        lst2 = []
        tmp = VectorChain(lst)
        lst2.append(tmp)
        angle = 0
        for i in range(1, detalization):
            lst2.append(lst2[-1].create_rotation(pi/detalization,
                vector.Vector3D(0,1,0), self._center)) 
        return lst2
    
    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

class Cube(shapes.Cube):

    def __init__(self, a_side:float, center: 'vector.Vector3D'):
        shapes.Cube.__init__(self, a_side)
        self._center = center
        self._chain = self.create_vector_chain()

    def create_vector_chain(self):
        lst = [[],[]]
        lst2 = [[],[],[],[]]
        zip1 = [-1, -1, 1, 1]
        zip2 = [-1, 1, 1, -1]
        for i,j in zip(zip1, zip2):
            lst[0].append(vector.Vector3D(i * self.a_side/2,
                j * self.a_side/2, 0) + self._center) 
        for i,j in zip(zip1, zip2):
            lst[1].append(vector.Vector3D(i * self.a_side/2, j * self.a_side/2,
                self.a_side) + self._center) 

        for i in range(4):
            lst2[i].append(lst[0][i])
            lst2[i].append(lst[1][i])
        lst = lst + lst2
        for i in range(len(lst)):
            lst[i] = VectorChain(lst[i])
        return lst

    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

class Parallelepiped(shapes.Parallelepiped):

    def __init__(self, a_side:float, b_side:float, c_side:float, center: 'vector.Vector3D'):
        shapes.Parallelepiped.__init__(self, a_side, b_side, c_side)
        self._center = center
        self._chain = self.create_vector_chain()

    def create_vector_chain(self):
        lst = [[],[]]
        lst2 = [[],[],[],[]]
        zip1 = [-1, -1, 1, 1]
        zip2 = [-1, 1, 1, -1]
        for i,j in zip(zip1, zip2):
            lst[0].append(vector.Vector3D(i * self.a_side/2,
                j * self.b_side/2, 0) + self._center) 
        for i,j in zip(zip1, zip2):
            lst[1].append(vector.Vector3D(i * self.a_side/2, j * self.b_side/2,
                self.c_side) + self._center) 

        for i in range(4):
            lst2[i].append(lst[0][i])
            lst2[i].append(lst[1][i])
        lst = lst + lst2
        for i in range(len(lst)):
            lst[i] = VectorChain(lst[i])
        return lst

    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

class Pyramid(shapes.Pyramid):

    def __init__(self, side_a:float, side_b:float, height:float,
            center:'vector.Vector3D'):
        shapes.Pyramid.__init__(self, side_a, side_b, height)
        self._center = center
        self._chain = self.create_vector_chain()

    def create_vector_chain(self):
        chains = []
        lst = []
        lst.append(vector.Vector3D(0,0,0))
        lst.append(vector.Vector3D(self.a_side, 0,0))
        lst.append(vector.Vector3D(self.a_side, self.b_side,0))
        lst.append(vector.Vector3D(0, self.b_side, 0))
        high = vector.Vector3D(self.a_side/2, self.b_side/2, self.height)
        center = vector.Vector3D(0,0,0)
        center += high/5
        for vec in lst:
            center += vec/5 
        for i in range(len(lst)):
            lst[i] += self._center - center
        high += self._center - center
        chains.append(VectorChain(lst))
        for vertex in lst:
            chains.append(VectorChain([vertex, high]))
        return chains

    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

class Cylinder(shapes.Cylinder):

    def __init__(self, radius:float, height:float, center:'vector.Vector3D'):
        shapes.Cylinder.__init__(self,radius, height)
        self._center = center
        self._chain = self.create_vector_chain(50)

    def create_vector_chain(self, detalization:int):
        lst = [[],[]]
        angle = 2 * pi / detalization
        sum_angle = 0
        for i in range(detalization):
            lst[0].append(self._center + vector.Vector3D(self.radius * cos(sum_angle),0,
                self.radius * sin(sum_angle)))
            sum_angle += angle
        sum_angle = 0
        for i in range(detalization):
            lst[1].append(self._center + vector.Vector3D(self.radius * cos(sum_angle),
                self.height,
                self.radius * sin(sum_angle)))
            sum_angle += angle
        chains = [VectorChain(lst[0]), VectorChain(lst[1])]
        for i in range(len(lst[0])):
            chains.append(VectorChain([lst[0][i], lst[1][i]]))
        return chains

    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

class Cone(shapes.Cone):

    def __init__(self, radius:float, height:float, center:'vector.Vector3D'):
        shapes.Cone.__init__(self, radius, height)
        self._center = center
        self._chain = self.create_vector_chain(50)

    def create_vector_chain(self, detalization:int):
        lst = []
        angle = 2 * pi / detalization
        sum_angle = 0
        for i in range(detalization):
            lst.append(self._center + vector.Vector3D(self.radius * cos(sum_angle),0,
                self.radius * sin(sum_angle)))
            sum_angle += angle
        chains = [VectorChain(lst)]
        high = self._center + vector.Vector3D(0,0,self.height)
        for i in range(len(lst)):
            chains.append(VectorChain([lst[i], high]))
        return chains

    def rotate(self, vector_rot: 'vector.Vector3D', angle:float):
        for chain in self._chain:
            chain = chain.rotate(angle, vector_rot, self._center)
    
    def draw(self, canvas:'Canvas'):
        for chain in self._chain:
            chain.draw(canvas)

   
