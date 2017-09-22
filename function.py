import random


# Function initNbPlayer() who define how number of player in the game
def initNbPlayer():
    nbPlayer = input("How many player ? : ")

    while (nbPlayer not in "2,3,4,5"  or len(nbPlayer) != 1): # Accept only 2-5 and block 2
        print("Please enter a correct number.")
        nbPlayer = input("How many player ? : ")

    # print(nbPlayer)
    return nbPlayer




import random
# Function initFirstPlayer() who define who start
def initFirstPlayer(nbPlayer):
     firstPlayer = random.randrange(1, int(nbPlayer), 1) # Function Random with (start, stop, step)
     print("The player " + str(firstPlayer) + " start the game.")

     return firstPlayer



# Function whereIsLeonard()
def whereIsLeonard():
    #Retourner le currentPlayer en fonction de si l'invention est terminé.
    while ()


#We need to have the inventionsList
def pickCardByAge(nbCards, age):
    listToReturn = []
    cardsLeftToPick = nbCards
    while(cardsLeftToPick >= 0):
        position = random.randrange(0, len(inventionsList)-1, 1)
        card = inventionsList[position]
        if card.age == age:
            inventionsList.remove(card)
            listToReturn.append(card)
            cardsLeftToPick = cardsLeftToPick-1