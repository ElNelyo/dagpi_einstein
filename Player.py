import parse
class Player:

    def __init__(self, name, ia):
        self.Name = name
        self.IA = ia
        self.associatedTeam = None
        self.active = False

    def chooseTeam(self, colorChose):
        for team in parse.Parse.myListTeam:
            if colorChose == team.color:
                self.myTeam = team


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
