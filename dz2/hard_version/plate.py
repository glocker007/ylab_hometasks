class Plate:
    def __init__(self):
        self._plate = [[0 for i in range(10)] for j in range(10)]

    def change(self, i, j, sign):
        if  (i <= 9) and (i >= 0) and (j <= 9) and (j >= 0): 
            if self.get(i,j) != 0:
                return False
            self._plate[i][j] = sign
            return True
        return False
    
    def unset(self, i, j):
        if (i >= 0) and (i <= 9) and (j >= 0) and (j <= 9):
            if self._plate[i][j] == 0:
                return False
            self._plate[i][j] = 0
            return True
        return False

    def get(self, i, j):
        return self._plate[i][j]
