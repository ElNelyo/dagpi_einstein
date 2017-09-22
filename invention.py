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
        # The age is calculated from the sum of each invention knowledge


# GETTER TESTS
invention = Invention('name', 'classification')
print('-')
print(invention.id)
print(invention.name)
print(invention.classification)
print(invention.age)
print('-')

# SETTER TESTS
invention.name = 'name2'
invention.classification = 'classification2'
invention.age = '1'
print('-')
print(invention.id)
print(invention.name)
print(invention.classification)
print(invention.age)
print('-')