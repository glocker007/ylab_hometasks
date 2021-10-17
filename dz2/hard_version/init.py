from game import Game
from agents import AgentClient, AgentGreedy

agent_1 = AgentClient()
agent_2 = AgentGreedy()
agent_3 = AgentGreedy()
lst = [agent_2, agent_1]
print("choose a sign [X/O]: ")
s = input()
if s == "X":
    lst[0], lst[1] = lst[1], lst[0]
game = Game(*lst)
game.start_game()
