class Invention:
    def __init__(self, name, classification, knowledge):
        self.name = name
        self.classification = classification
        self.knowledge = knowledge
        self.generalKnowledgeColors = []
        for kn in knowledge:
            preciseKnowedgeColor = []
            for i in range(0, int(kn)):
                preciseKnowedgeColor.append((255, 255, 255))
            self.generalKnowledgeColors.append(preciseKnowedgeColor)

        self.age = 0
        # The age is calculated from the sum of each invention knowledge


# GETTER TESTS
#invention = Invention('name', 'classification')
#print('-')
#print(invention.name)
#print(invention.classification)
#print(invention.age)
#print('-')

# SETTER TESTS
#invention.name = 'name2'
#invention.classification = 'classification2'
#invention.age = '1'
#print('-')
#print(invention.name)
#print(invention.classification)
#print(invention.age)
#print('-')