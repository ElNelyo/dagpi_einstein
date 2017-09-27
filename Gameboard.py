# Create Gameboard class
import parse
import random
import function

class Gameboard:
    age = 0
    cardsOnBoard            = []
    playersOnBoard          = []
    pocket                  = []
    emplacementOnBoard      = []
    possibleactions         = []
    currentPlayer = 0

    def __init__(self, tour, listPlayer):
        self.tour = tour
        self.age = 1
        self.playersOnBoard = listPlayer
        self.nbCardToDistribute = len(self.playersOnBoard) + 3
        self.currentPlayer = len(self.playersOnBoard)-1
        for token in parse.Parse.myListReward:
            self.pocket.append(token)

    def awakeCurrentPlayer(self):
        function.Function.awake(self, self.playersOnBoard[self.currentPlayer].myTeam.inventors)
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
    def newTurn(self,team):
        print("LLALLALLALL")
        self.possibleactions = (Function.all_possible_action(self,team,self.cardsOnBoard))






    """def truc(self):
        for card in self.cardsOnBoard:
            print("----------------------")
            print(card.name)
            for knowl in card.knowledge:
                print(knowl)
    """





