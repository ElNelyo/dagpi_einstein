from enum import Enum,unique


@unique
class Action(Enum):
    """ enumeration class that enumerates the possible colors """
    IOI=0
    REFRESH=1
    PROGRESSREWARDPUTOTHER=2 #Two different enum for PROGRESREWARD, one for value=1, one for the others
    PROGRESSREWARDPUT1=3
    USECOFFEE=4
    USEBONUSCUBE=5

