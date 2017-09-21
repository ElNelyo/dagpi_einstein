import Knowledge
import Invention

class InventionKnowledge:
    def __init__(self,Knowledge,Invention,nbCube):
        self.Knowledge = Knowledge
        self.Invention = Invention
        self.nbCube = 0

#TESTS
knowledge1 = Knowledge.Knowledge
invention1 = Invention.Invention(1,'invention1','classification1')
inventionKnowledge1 = InventionKnowledge(knowledge1,invention1,1)
print('-')
print(inventionKnowledge1.Knowledge.Physics.value)
print(inventionKnowledge1.Knowledge.Mathematics.value)
print(inventionKnowledge1.Invention.name)
print(inventionKnowledge1.Invention.classification)
print(inventionKnowledge1.Invention.age)
print('-')