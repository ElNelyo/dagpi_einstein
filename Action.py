from enum import Enum,unique


@unique
class Action(Enum):
    """ enumeration class that enumerates the possible colors """
    IOI=0
    REFRESH=1
    PROGRESSREWARD=2
    USECOFFEE=3
    USEBONUSCUBE=4

