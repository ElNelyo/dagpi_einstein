class Invention:
    def __init__(
            self,
            id,
            name,
            classification,


    ):
        self.id = id
        self.name = name
        self.classification = classification
        self.age = 0
        # L'age est calculé par rapport aux compétences


# TESTS GETTER
invention = Invention('id', 'name',' classification')
print('-')
print(invention.id)
print(invention.name)
print(invention.classification)
print(invention.age)
print('-')

# TESTS SETTER
invention.id = 'id2'
invention.name = 'name2'
invention.classification = 'classification2'
invention.age = '1'
print('-')
print(invention.id)
print(invention.name)
print(invention.classification)
print(invention.age)
print('-')