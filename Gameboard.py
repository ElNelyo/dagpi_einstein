# Create Gameboard class
import parse
import random


class Gameboard:
    age = 0
    cardsOnBoard            = []
    playersOnBoard          = []
    pocket                  = []
    emplacementOnBoard      = []

    def __init__(self, tour, nbPlayer):
        self.tour = tour
        self.age = 1
        self.nbCardToDistribute = (nbPlayer + 3)
        for token in parse.Parse.myListReward:
            self.pocket.append(token)

    def distribute(self):
        cards = parse.Parse()
        cards = cards.getInvention()
        cpt = 0

        while cpt < self.nbCardToDistribute:
            myCard = cards[random.randint(0, len(cards))-1]
            if self.age == myCard.age:
                print(myCard.name)
                self.cardsOnBoard.append(myCard)
                temporarylist = []
                token1 = self.pocket[random.randint(0, len(self.pocket)-1)]
                self.pocket.remove(token1)

                token2 = self.pocket[random.randint(0, len(self.pocket) - 1)]
                self.pocket.remove(token2)
                temporarylist.append(myCard)
                temporarylist.append(token1)
                temporarylist.append(token2)
                self.emplacementOnBoard.append(temporarylist)

                cards.remove(myCard)
                cpt += 1

        return self.cardsOnBoard

    def wakeUp(self, player, coffee, inventor):
        if coffee and not inventor:
            for inventor in player.myTeam.inventors:
                inventor.sleep = False
        else:
            inventor.sleep = True



    """def truc(self):
        for card in self.cardsOnBoard:
            print("----------------------")
            print(card.name)
            for knowl in card.knowledge:
                print(knowl)
    """





