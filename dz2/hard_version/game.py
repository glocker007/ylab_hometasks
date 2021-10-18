from environment import Environment

class Game(Environment):
    def __init__(self, agent_1, agent_2):
        super().__init__()
        self.agents = [agent_1, agent_2]

    def move(self):
        e = self.agents[self.count % 2].choose_move(self)
        is_end = self.make_a_move(e)
        return is_end

    def restart(self):
        print("Restart game ? [Y/ N]:") 
        s = input()
        if s == "Y":
            print("Swap sides? [Y/N]:") 
            s = input()
            if s == "Y":
                self.agents[0], self.agents[1] = self.agents[1], self.agents[0]
            self.__init__(self.agents[0], self.agents[1])
            print(self.count)
            return True
        else:
            return False


    def start_game(self):
        self.Print()
        while True:
            if len(self.unused_fields) == 0:
                self.Print()
                print("Draw")
                self.who_won()
                go_on = self.restart()
                if go_on:
                    self.Print()
                    continue
                else:
                    break
            flag = self.move()
            self.Print()
            if flag:
                self.Print()
                self.who_won()
                go_on = self.restart()
                if go_on:
                    self.Print()
                    continue
                else:
                    break


    def who_won(self):
        if self.count % 2 == 0:
            print("X - s won")
        else:
            print("O - s won")


    def Print(self):
        string = ""
        for i in range(10):
            for j in range(10):
                string += "----"
            string += "-\n"
            for j in range(10):
                s = self.get(i, j)
                if s == 0:
                    if i == 0:
                        string += "| " + str(i*10 + j) + " "
                    else:
                        string += "|" + str(i*10 + j) + " "
                else:
                    if s == 1:
                        string += "| O "
                    else:
                        string += "| X "
            string += "|\n"
        for i in range(10):
            string += "----"
        string += '-\n'
        print(string)
