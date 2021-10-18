import random

class AgentClient:
    def choose_move(self, game):
        print("choose the number = ")
        try:
            i = int(input())
            i, j = i // 10, i % 10
        except Exception:
            print("incorrect input")
            return self.choose_move(game)
        if game.is_legal((i, j)):
            return (i, j)
        else:
            print("move is illegal")
            return self.choose_move(game)

class AgentGreedy:
    def choose_move(self, game):
        lst = list(game.unused_fields)
        random.shuffle(lst)
        for e in lst:
            if game.check_is_terminal(e):
                continue 
            else:
                return e
        return lst[0]
