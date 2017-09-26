import parse
class Player:

    def __init__(self, name, ia, associatedTeam,active):
        self.Name = name
        self.IA = ia
        self.associatedTeam = None
        self.active = False

    def chooseTeam(colorChose):
        for team in parse.Parse.myListTeam:
            if colorChose == team.color:
                self.myTeam = team
                team.playerName = player1.Name

    def displayTruc(self):
        print("HELLO DARKNESS MY OLD FRIEND")


class Human(Player):
    def play(self):
        return

class AI(Player):
    def play(self):
        return

class AIBasic(AI):
    def play(self):
        return

class AIAdvanced(AI):
    def play(self):
        return
