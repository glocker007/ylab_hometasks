from decimal import Decimal

class Point():
    def __init__(self, x_, y_):
        self.x = Decimal(x_)
        self.y = Decimal(y_)
    def __getitem__(self, idx):
        if (idx == 0):
            return self.x
        else:
            return self.y
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__()
    def r(self):
        return (self.x**2 + self.y**2)**Decimal(0.5)
        

def permutations(elements):
    if len(elements) <= 1:
        yield(elements)
    else:
        for perm in permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def Calculate(trace, points):#example trace [1, 2, 5, 3, 4]
    Sum = Decimal(0.00000000000)
    l = len(trace)
    for i in range(l):
       Sum += (points[trace[(i + 1)%l]] - points[trace[i%l]]).r() 
    return Sum

if __name__ == "__main__":
    elements = [1, 2, 3, 4]
    points = [Point(0,2), Point(2, 5), Point(5, 2), Point(6, 6), Point(8, 3)]

    Min_distance = 10e9

    for perm in permutations(elements):
        d = Calculate([0] + perm, points)
        if d < Min_distance:
            Min_perm = [0] + perm
            Min_distance = d

    Min_perm = Min_perm + [0]
    l = len(Min_perm)
    Sum = Decimal(0.000000)

    for i in range(l):
        if i == 0:
            print(points[Min_perm[i]], end = " -> ")
        else:
            Sum += (points[Min_perm[(i) % l]] - points[Min_perm[(i-1)%l]]).r()
            print(points[Min_perm[i%l]], end = f"[{round(Sum, 16)}]")
            if (i == l-1):
                print(f" = {Sum}")
            else:
                print(" -> ", end = "")
