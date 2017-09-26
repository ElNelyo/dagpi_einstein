import random
import parse
from Knowledge import Knowledge
from Inventor import Inventor
from Action import Action


# Function initNbPlayer() who define how number of player in the game
def initNbPlayer():
    nbPlayer = input("How many player ? : ")

    while (nbPlayer not in "2,3,4,5" or len(nbPlayer) != 1):  # Accept only 2-5 and block 2
        print("Please enter a correct number.")
        nbPlayer = input("How many player ? : ")

    # print(nbPlayer)
    return nbPlayer



# Function initFirstPlayer() who define who start
def initFirstPlayer(nbPlayer):
    firstPlayer = random.randrange(1, int(nbPlayer), 1)  # Function Random with (start, stop, step)
    print("The player " + str(firstPlayer) + " start the game.")

    return firstPlayer


# Function whereIsLeonard()
'''
def whereIsLeonard():
    #Retourner le currentPlayer en fonction de si l'invention est terminé.
    while ()
'''


# We need to have the inventionsList
def pickCardByAge(nbCards, age):
    listToReturn = []
    cardsLeftToPick = nbCards
    while (cardsLeftToPick >= 0):
        position = random.randrange(0, len(parse.Parse.inventionslist) - 1, 1)
        card = parse.Parse.inventionslist[position]
        if card.age == age:
            parse.Parse.inventionslist.remove(card)
            listToReturn.append(card)
            cardsLeftToPick = cardsLeftToPick - 1



# Wake up all the inventors of a team
def awake(myTeam):
    for inventor in myTeam:
        if inventor.sleep == True:
            inventor = False


# shut down an inventor
def goToSleep(myInventor):
    if myInventor.sleep == False:
        myInventor.sleep = True


# pas fini
'''def changePlayer(nbPlayer, firstPlayer):
    currentPlayer= firstPlayer
'''

#Return a list of possible actions for a user on a team
def all_possible_action(myTeam, myCardBoard):
    allPossibleAction = []
    cptAwake = 0
    for inventor in myTeam.inventors:
        if not inventor.sleep:
            #listCompatibleInventions est la liste d'inventions du plateau compatible avec l'inventeur
            listCompatibleInventions = inventor.boardCardsForInventor(myCardBoard)
            for invention in listCompatibleInventions:
                ioilist=[]
                ioilist.append(Action.IOI)
                ioilist.append(inventor)
                ioilist.append(invention)
                allPossibleAction.append(ioilist)

        if inventor.sleep==True:
            cptAwake +=1

    if cptAwake>0:
        awakeList = []
        awakeList.append(Action.AWAKE)
        awakeList.append("Recycle")
        allPossibleAction.append(awakeList)
        awakeList = []
        awakeList.append(Action.AWAKE)
        awakeList.append("Coffee")
        allPossibleAction.append(awakeList)


    for a in allPossibleAction:
        print(a[0].name)
        print(a[1].name)
        print(a[2].name)
    print(allPossibleAction)

    for team in parse.Parse.myListTeam:
        print(team.color)


'''
        all_possible_action.append(liste(inventeur/invention/liste [0,0,0,0]
                                         ))
         for token in myTokens:
             if token.type == progress_reward
'''
all_possible_action(parse.Parse.myListTeam[0], parse.Parse.myListInvention)
