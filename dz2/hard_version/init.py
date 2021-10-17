from game import Game
from agents import AgentClient, AgentGreedy

agent_1 = AgentClient()
agent_2 = AgentGreedy()
agent_3 = AgentGreedy()
game = Game(agent_2, agent_1)
game.start_game()
