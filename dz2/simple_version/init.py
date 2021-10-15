from game import Game
from environment import Environment
from agents import AgentClient, AgentGreedy

a_1 = AgentClient()
a_2 = AgentGreedy()
a_3 = AgentGreedy()
print("Choose a sign [x/o]:")
s = input()
agents = [a_1, a_2]
if s == "x":
    agents[0], agents[1] = agents[1], agents[0]
game = Game(Environment(), agents[0], agents[1])
game.start_game()
