import Knowledge
import invention


class InventionKnowledge:
    def __init__(self, Knowledge, Invention):
        self.Knowledge = Knowledge
        self.Invention = Invention
        self.nbCube = 0

    def getAge(self, Invention):
        age = 0
        for k in Knowledge.getValues():
            age = age+k
        return age

# TESTS
