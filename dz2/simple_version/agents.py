import random


class AgentClient:
    def choose_move(self, env):
        print("choose coords (splited by space): ", end=" ")
        while True:
            s = input()
            if len(s.split()) == 0:
                s = input()
            else:
                i, j = map(int, s.split())
                break
        is_end, correct = env.peek_a_move((i, j))
        if not correct:
            print("not a move")
            return self.choose_move(env)
        return (i, j), is_end


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
