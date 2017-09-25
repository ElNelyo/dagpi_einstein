import parse
class Player:

    def __init__(self, name, ia):
        self.Name = name
        self.IA = ia

    def chooseTeam(colorChose):

        player1 = Player.Player("player1", False)

        for team in parse.Parse.myListTeam:
            if colorChose == team.color:
                player1.team = team
                team.playerName = player1.Name


