import random

"""
    client agent 
"""

class AgentClient:
    def choose_move(self, env):
        def is_number(char):
            if len(char) != 1:
                return False
            if ord(char) <= ord('9') and ord(char) >= ord('0'):
                return True
            return False

        print("choose coords (splited by space): ", end=" ")
        while True:
            s = input()
            if len(s.split()) == 0:
                print("not a numbers")
                return self.choose_move(env)
            else:
                splited = s.split()
                if len(splited) == 2 and is_number(splited[0]) and is_number(splited[1]):
                    i, j = map(int,splited)
                    break
                else:
                    return self.choose_move(env)

        is_end, correct = env.peek_a_move((i, j))
        if not correct:
            print("not a move")
            return self.choose_move(env)
        return (i, j), is_end

"""
    Just a simple greedy algorithm
"""

class AgentGreedy:
    def choose_move(self, env):
        lst = list(env.unused_fields())
        random.shuffle(lst)
        for e in lst:
            is_end, correct = env.peek_a_move(e)
            if correct:
                if not is_end:
                    return e, False
                else:
                    continue
            else:
                continue
        return lst[0], True
