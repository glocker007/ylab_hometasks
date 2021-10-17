from plate import Plate


"""
    checks , is move is terminal or not 
"""

class Environment(Plate):
    def __init__(self):
        super().__init__()
        self.unused_fields = set([(i, j) for i in range(10) for j in range(10)])
        self.count = 0

    def check_is_terminal(self, move):
        if self.check_lines(move):
            return True
        return False

    def check_lines(self, move):
        if self.check_vertical(move):
            return True
        if self.check_horisontal(move):
            return True
        if self.check_diagonal_down_right(move):
            return True
        if self.check_diagonal_up_right(move):
            return True
        return False
    
    

    def check_vertical_horisontal(self, move, shape):
        sign = self.whos_turn()
        if self.is_legal(move):
            changed = self.change(move[0], move[1], sign)
            in_a_row = 0
            for j in range(10):
                if ((shape == 0) * self.get(j, move[1]) +
                   (shape == 1) * self.get(move[0], j)) == sign:
                    in_a_row += 1 
                    if in_a_row == 5:
                        if changed:
                            self.unset(move[0], move[1])
                        return True
                else:
                    in_a_row = 0
            if changed:
                self.unset(move[0], move[1])
            return False
        return False

    def check_vertical(self, move):
        return self.check_vertical_horisontal(move, 0) 
    
    def check_horisontal(self, move):
        return self.check_vertical_horisontal(move, 1) 

   
    def check_diagonals(self, move, shape):
        if self.is_legal(move):
            def possible(i ,j):
                if i <= 9 and i >= 0:
                    if j <= 9 and j >= 0:
                        return True
                    return False
                return False
            
            sign = self.whos_turn()
            start_i = move[0]
            start_j = move[1]
            
            if shape == 0:
                inc = -1
                d = start_i - start_j
                N = 10 - abs(d)
            else:
                inc = 1
                d = start_i + start_j
                N = 10 - abs(d - 9)
                 
            while possible(start_i, start_j):
                start_i += inc
                start_j -= 1
            start_i -= inc
            start_j += 1
            
            in_a_row = 0
            if self.get(start_i, start_j) == sign:
                in_a_row += 1

            changed = self.change(move[0], move[1], sign)

            for j in range(N - 1):
                if in_a_row == 5:
                    return True
                start_i -= inc
                start_j += 1
                if self.get(start_i, start_j) == sign:
                    in_a_row += 1
                    if in_a_row == 5:
                        if changed:
                            self.unset(move[0], move[1])
                        return True
                else:
                    in_a_row = 0
            return False
        return False
    
    def check_diagonal_down_right(self, move): 
        return self.check_diagonals(move, 0)
    
    def check_diagonal_up_right(self, move):
        return self.check_diagonals(move, 1)

    def is_legal(self, move):
        if move in self.unused_fields:
            return True
        return False
    
    def whos_turn(self):
        if self.count % 2:
            return 1
        return -1

    def make_a_move(self, move):
        sign = self.whos_turn()
        is_end = False
        if self.is_legal(move):
            is_end = self.check_is_terminal(move) 
            self.change(move[0], move[1], sign)
            self.unused_fields.discard(move)
            self.count += 1
        return is_end
