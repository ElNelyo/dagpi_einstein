import Player
import InventionKnowledge
import Knowledge
import Invention

class InventionKnowledgePlayer:
    def __init__(self, player, inventionKnowledge, nbCube):
        self.Player = player
        self.InventionKnowledge = inventionKnowledge
        self.NombreCube = 0


# TESTS
player1 = Player.Player(1, 'thomas')
knowledge1 = Knowledge.Knowledge
invention1 = Invention.Invention(1, 'invention1', 'classification1')
inventionKnowledge1 = InventionKnowledge.InventionKnowledge(knowledge1, invention1, 1)
inventionKnowledgePlayer1 = InventionKnowledgePlayer(player1, inventionKnowledge1, 2)
print('-')
print(inventionKnowledgePlayer1.Player.nom)
print(inventionKnowledgePlayer1.InventionKnowledge.Invention.name)
print(inventionKnowledgePlayer1.InventionKnowledge.Invention.classification)
print(inventionKnowledgePlayer1.InventionKnowledge.Invention.age)
print(inventionKnowledgePlayer1.InventionKnowledge.Invention.classification)
print(inventionKnowledgePlayer1.InventionKnowledge.Knowledge.Mathematics.value)
print('-')
