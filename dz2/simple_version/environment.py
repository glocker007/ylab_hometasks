class Environment:
    def __init__(self):
        self._unused_squares = set()
        for i in range(10):
            for j in range(10):
                self._unused_squares.add((i, j))
        self._used_by_x = set()
        self._used_by_o = set()
        self._plate = [[0 for i in range(10)] for j in range(10)]
        # 1 for x | -1 for o
        self.count = 0
        self._range = 5
        self._terminated = False

    def unused_fields(self):
        return self._unused_squares

    def is_terminal(self):
        return self._terminated

    def reset(self):
        self.__init__()

    def whos_turn(self):
        if self.count % 2 == 1:
            return -1
        else:
            return 1

#   def used_by_x(self):
#        return self._used_by_x

#   def used_by_o(self):
#        return self._used_by_o

    def plate(self):
        return self._plate

    """peeks a move, and checks 
    whether game is ended or not,
    return boolean
    """
    def peek_a_move(self, move):  # Game_ended? # Game Interrupted?
        sign = self.whos_turn()
        if self.__is_move_legit(move) and not self._terminated:
            self._plate[move[0]][move[1]] = sign
            self.count += 1
            flag = self.__is_terminal(move)
            self.count -= 1
            self._plate[move[0]][move[1]] = 0
            if flag:
                return True, True
            else:
                return False, True
        else:
            return False, False

    """takes a tuple as an input, 
    and makes a move"""
    def make_a_move(self, move):
        if self.__is_move_legit(move) and not self._terminated:
            self.__change(move)
            self.count += 1
            if self.__is_terminal(move):
                self._terminated = True
                return True
            return True
        return False

#    def __PrintGratitude(self):
#        if (self.count % 2 == 1):
#            print("won zeros !!")
#        else:
#            print("won x-s!!")


    """ It takes tuple as an input , and 
    returns answer whether games is terminated or not """
    def __is_terminal(self, move):
        sign = -1 * self.whos_turn()
        begin, v, numbers = self.__start_line(move)

#   move is already done , the last pixel is known
        for i in range(4):
            if self.__check_line(begin[i], numbers[i], v[i], sign):
                return True
        return False

    def __boundaries(self, shape, move):
        min_ = max(0, move[shape] - self._range + 1)
        max_ = min(9, move[shape] + self._range - 1)
        return min_, max_

    def __change(self, move):
        sign = self.whos_turn()
        self._plate[move[0]][move[1]] = sign
        if sign == 1:
            self._used_by_x.add(move)
        else:
            self._used_by_o.add(move)
        self._unused_squares.discard(move)

    """
        calculates begin as a list of tuples, 
        numbers - count of squares in each line as list of ints
        vectors - list of tuples that contain the direction of line 
        for the horizontal, vertical , and two diagonal lines 
        and returns them all 
    """

    def __start_line(self, move):
        d = move[1] - move[0]
        start_d_1 = (-1 * min(0, d), max(0, d))
        d = move[1] + move[0]
        start_d_2 = ((d < 9) * d + (d >= 9) * 9, ((d > 9) * (d - 9)))
        starts = [(move[0], 0), (0, move[1]), start_d_1, start_d_2]
        vectors = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        numbers = [10, 10,
                   10 - abs(move[1] - move[0]),
                   10 - abs(move[1] + move[0] - 9)]
        return starts, vectors, numbers

    """
    takes as input prevous method single output, 
    and checks is move is terminal
    """

    def __check_line(self, start, n, v, sign):
        in_a_row = 0
        start_i = start[0]
        start_j = start[1]
#   print(start_i, start_j)
        if self._plate[start_i][start_j] == sign:
            in_a_row += 1
        for i in range(n - 1):
            if in_a_row == self._range:
                return True
            start_i += v[0]
            start_j += v[1]
            if self._plate[start_i][start_j] == sign:
                in_a_row += 1
            else:
                in_a_row = 0
        if in_a_row >= self._range:
            return True
        return False

    def __is_move_legit(self, move):
        if move in self._unused_squares:
            return True
        return False

    def __str__(self):
        string = " "
        for j in range(10):
            string += " | "+str(j)+""
        string += " |\n  "
        for j in range(10):
            string += " ---"
        string += " \n"
        for i in range(10):
            string += str(i)+" |"
            for j in range(10):
                if self._plate[i][j] == 1:
                    string += " x |"
                elif self._plate[i][j] == 0:
                    string += "   |"
                else:
                    string += " o |"
            string += "\n  "
            for j in range(10):
                string += " ---"
            string += " \n"
        return string + "\n terminated: " + str(self._terminated)
