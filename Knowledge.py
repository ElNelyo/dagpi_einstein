from enum import Enum, unique


@unique
class Knowledge(Enum):
    physics = 0
    chemistry = 1
    mechanics = 2
    mathematics = 3
