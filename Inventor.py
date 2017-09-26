import Knowledge

class Inventor:

    # Init inventor with his name and victory points
    def __init__(self, name, points, currentKnowledge, targetknowledge):
        self.name = name
        self.points = points
        self.currentKnowledge = currentKnowledge
        self.targetknowledge = targetknowledge
        self.sleep = False


    def canAddKnowledge(self, know, value):
        return self.currentKnowledge[know] + 1 == value and value <= 4

    def addKnowledge(self, know, value):
        if self.canAddKnowledge(know, value):
            self.currentKnowledge[know] = self.currentKnowledge[know] + 1
