import Player, Inventor, Color


class Team:
    def __init__(self, playerTeam, inventorTeam, colorTeam):
        self.player = playerTeam
        self.inventorTeam = []
        self.color = colorTeam
