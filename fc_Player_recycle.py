from Team import Team
from Inventor import Inventor
from Player import Player

from fc_Player_Awake import Awake




def recycle(PlayerZ):
    if PlayerZ.associatedTeam!= None:
        TeamZ = PlayerZ.associatedTeam
        Awake(TeamZ)
        PlayerZ.active = False
    else:
        print("Méthode indisponible : aucune team associée au Player !")