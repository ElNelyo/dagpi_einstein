from Player import Player
from Inventor import Inventor


# A mettre dans la classe Player

def Awake(PlayerZ):
    if PlayerZ.associatedTeam != None:

        teamZ = PlayerZ.associatedTeam
        for inventorX in teamZ.inventors:
            if inventorX.sleep == True:
                inventorX = False

        else:
            print("Méthode indisponible : aucune team associée au Player !")