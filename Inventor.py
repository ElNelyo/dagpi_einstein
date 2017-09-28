from Knowledge import Knowledge

class Inventor:

    # Init inventor with his name and victory points
    def __init__(self, name, points, currentKnowledge, targetKnowledge):
        self.name = name
        self.points = points
        self.currentKnowledge = currentKnowledge
        self.targetKnowledge = targetKnowledge
        self.sleep = False


    def canAddKnowledge(self, know, value):
        return self.currentKnowledge[know] + 1 == value and value <= 4

    def addKnowledge(self, know, value):
        if self.canAddKnowledge(know, value):
            self.currentKnowledge[know] = self.currentKnowledge[know] + 1

    #Return a list of inventions that fit with the inventor
    def boardCardsForInventor(self, cardBoard):
            # liste d'inventions compatibles à l'inventeur
        inventorInventionslist = []
        for invention in cardBoard:
            # Pour chaque compétence de Knowledge SI la compétence actuelle de l'invention est
            listKnowledge = []

            for competence in Knowledge:

                if invention.knowledge[competence.value] == 0 \
                        or self.currentKnowledge[competence.value] == 0 \
                        or self.sleep:
                    listKnowledge.append(0)

                else:
                    whiteSquares = []
                    for knowledgeColors in invention.generalKnowledgeColors:
                        nbWhite = 0
                        for i in  range(0, len(knowledgeColors)):
                            if knowledgeColors[i] == (255, 255, 255):
                                nbWhite += 1
                        whiteSquares.append(nbWhite)
                    a = min(whiteSquares[competence.value], self.currentKnowledge[competence.value])
                    listKnowledge.append(a)


            if listKnowledge != [0, 0, 0, 0]:
                inventorInventionslist.append(invention)

        return inventorInventionslist