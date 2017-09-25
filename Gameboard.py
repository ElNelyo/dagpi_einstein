# Create Gameboard class
import parse
import random


class Gameboard:
    age = 0
    cardsOnBoard = []
    def __init__(self, tour, nbPlayer):
        self.tour = tour
        self.age = 1
        self.nbCardToDistribute = (nbPlayer +3)


    def distribute(self,age):
        cards = parse.Parse()
        cards = cards.getInvention()
        cpt = 0

        while cpt < self.nbCardToDistribute:
            myCard = cards[random.randint(0,len(cards))-1]
            if(age==1 and myCard.age==1):
                print(myCard.name)
                self.cardsOnBoard.append(myCard)
                cards.remove(myCard)
                print(myCard.age)
                cpt += 1
            elif(age==2 and myCard.age==2):
                print(myCard.name)
                self.cardsOnBoard.append(myCard)
                cards.remove(myCard)
                print(myCard.age)
                cpt += 1
            elif(age==3 and myCard.age==3):
                print(myCard.name)
                print(myCard.age)
                self.cardsOnBoard.append(myCard)
                cards.remove(myCard)
                cpt += 1

        


