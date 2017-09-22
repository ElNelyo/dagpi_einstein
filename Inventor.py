import Knowledge

class Inventor:

    # Init inventor with his name and victory points
    def __init__(self, name, points, startknowledge, targetknowledge):
        self.name = name
        self.points = points
        self.startknowledge = startknowledge
        self.targetknowledge = targetknowledge
        self.sleep = False


    def canAddKnowledge(self, know, value):
        return self.startknowledge[know]+1 == value and value<=4

    def addKnowledge(self, know, value):
        if self.canAddKnowledge(know, value):
            self.startknowledge[know] = self.startknowledge[know]+1
