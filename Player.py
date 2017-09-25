import parse
class Player:

    def __init__(self, name, ia):
        self.Name = name
        self.IA = ia

    def chooseTeam(colorChose):
        for team in parse.Parse.myListTeam:
            if colorChose == team.color:
                self.myTeam = team
                team.playerName = player1.Name


