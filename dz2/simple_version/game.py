class Game:
    def __init__(self, env, agent_1, agent_2):
        self._env = env
        self._a1 = agent_1
        self._a2 = agent_2
        self._count = 0

    def reset(self):
        self._env.reset()
        self._count = 0

    def make_a_move(self):
        if self._count % 2 == 1:
            agent = self._a1
        else:
            agent = self._a2

        if len(self._env.unused_fields()) == 0:
            print("Draw")
            return True
        e, is_end = agent.choose_move(self._env)
        if is_end:
            sign = self._env.whos_turn()
            self._env.make_a_move(e)
            print(e, "<- last move")
            s = "x"
            if sign == 1:
                s = "o"
            print("Won ", s, " !!")
            return True
        self._env.make_a_move(e)
        self._count += 1
        return False

    def start_game(self):
        while True:
            print(self._env)
            flag = self.make_a_move()
            if flag:
                print(self._env)
                print("continue? [Y/N]?", end="")
                c = input()
                if c == "Y":
                    print("swap sides? [Y/N]")
                    s = input()
                    if s == "Y":
                        self._a1, self._a2 = self._a2, self._a1
                    self.reset()
                    continue
                else:
                    break
        print(self._env)
