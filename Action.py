from enum import Enum,unique


@unique
class Action(Enum):
    """ enumeration class that enumerates the possible colors """
    IOI=0
    AWAKE=1
    CONSUMETOKEN=2
