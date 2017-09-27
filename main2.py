#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
import pygame
import random
from list import list
from button import button
from sprite import sprite
from label import label
from Gameboard import Gameboard
from Inventor import Inventor
from hollowRect import hollowRect


class Game:

    # Colors
    CIEL = 0, 200, 255
    BLUE = 0, 102, 255
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    YELLOW = 255, 255, 100
    PURPLE = 204, 0, 153
    GRAY = 150, 150, 150

    # Screen sizes
    WIDTH = 1080
    HEIGHT = 720

    #Sizes of splited screen in 4/2
    WINDOW_WIDTH = WIDTH / 4
    WINDOW_HEIGHT = HEIGHT / 2

    #Size of buttons
    WIDTH_BUTTON = 100
    HEIGHT_BUTTON = 50

    # Height of a line
    ONELINE = 12

    # List of everything to display
    toDisplay = []

    def __init__(self):
        pygame.init()

    def updateDisplay(self, displayList, fenetre):

        fenetre.fill(Game.WHITE)

        for element in displayList:

            if element.name == "buttons":
                for butt in element.l:
                    butt.display(fenetre)

            if element.name == "sprites":
                for spr in element.l:
                    spr.display(fenetre)

            if element.name == "labels":
                for l in element.l:
                    print(l.text)
                    l.display(fenetre)

            if element.name == "hollowRect":
                for hRect in element.l:
                    hRect.display(fenetre)

        pygame.display.flip()

    def loadSettingMenu(self):

        playerColor = 0

        clock = pygame.time.Clock()

        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        back = pygame.image.load("background.jpg").convert()
        back2 = pygame.transform.scale(back, (int(Game.WIDTH), int(Game.HEIGHT)))
        back3 = sprite(0, 0, back2)

        menuSprites = list([back3], "sprites")


        Game.toDisplay.append(menuSprites)

        strColors = ["GREEN", "BLUE", "PURPLE", "RED", "YELLOW"]
        rgbColors = [Game.GREEN, Game.BLUE, Game.PURPLE, Game.RED, Game.YELLOW]

        buttons = list([], "buttons")

        for i in range(0, 5):
            b = button(Game.WIDTH/6 * (i + 1) - Game.WIDTH_BUTTON / 2,
                       Game.HEIGHT / 4,
                       Game.WIDTH_BUTTON,
                       Game.HEIGHT_BUTTON,
                       rgbColors[i],
                       strColors[i],
                       14)
            buttons.l.append(b)

        Game.toDisplay.append(buttons)

        menuLabel = list([], "labels")

        text = "Select a player!"

        lab = label((Game.WIDTH - len(text)*26) / 2, Game.HEIGHT / 5 - 26, text, 52)

        menuLabel.l.append(lab)

        Game.toDisplay.append(menuLabel)

        loop = True

        while loop:

            self.updateDisplay(Game.toDisplay, fenetre)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for li in Game.toDisplay:
                        if li.name == "buttons":
                            for b in li.l:
                                if b.intersect(event.pos):
                                    playerColor = b.settings[4]
                                    loop = False
        return playerColor

    def selectIANumber(self, playerColor):

        # Remove buttons, keep background and menuLabel
        Game.toDisplay.pop(1)

        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Update menuLabel
        Game.toDisplay[1].l[0].text = "Select max numbers of players"
        text = Game.toDisplay[1].l[0].text
        Game.toDisplay[1].l[0].posX = (Game.WIDTH - len(text)*26) / 2
        Game.toDisplay[1].l[0].posY = Game.HEIGHT / 5 - 26

        buttons = list([], "buttons")

        for i in range(0, 4):
            b = button(Game.WIDTH / 5 * (i + 1) - Game.WIDTH_BUTTON / 2,
                       Game.HEIGHT / 3,
                       Game.WIDTH_BUTTON,
                       Game.HEIGHT_BUTTON,
                       Game.WHITE,
                       str(i + 2),
                       14)
            buttons.l.append(b)

        Game.toDisplay.append(buttons)


        loop = True

        while loop:

            self.updateDisplay(Game.toDisplay, fenetre)

            nbPlayer = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for butt in Game.toDisplay[2].l:
                        if butt.intersect(event.pos):
                            loop = False
                            nbPlayer = int(butt.settings[5])  # get button label
        return nbPlayer

    def placePlayers(self, playerColor, nbPlayer):

        colorList = [Game.BLUE, Game.PURPLE, Game.YELLOW, Game.RED, Game.GREEN]
        colorList.remove(playerColor)

        returnColorList = []

        while len(returnColorList) != nbPlayer-1:
            i = random.randrange(0, len(colorList), 1)
            returnColorList.append(colorList[i])
            colorList.pop(i)

        returnColorList.append(playerColor)

        return returnColorList

    def loadGameSprites(self):
        back = pygame.image.load("background.jpg").convert()
        back2 = pygame.transform.scale(back, (int(Game.WINDOW_WIDTH * 3), int(Game.WINDOW_HEIGHT)))
        back3 = sprite(0, Game.HEIGHT / 2, back2)

        menuSprites = list([back3], "sprites")

        fondCard = pygame.image.load("backgroundCard.png").convert()
        playerBackground = pygame.transform.scale(fondCard, (int(Game.WINDOW_WIDTH), int(Game.WINDOW_HEIGHT)))

        for i in range(0, 5):
            if i == 4:
                playerColorSprite = sprite((Game.WIDTH / 4) * 3, Game.HEIGHT / 2, playerBackground)
            else:
                playerColorSprite = sprite((Game.WIDTH / 4) * i, 0, playerBackground)
            menuSprites.l.append(playerColorSprite)
        return menuSprites

    def loadGameHollowRects(self, nbPlayer, playerColorsList):
        hollowRectList = list([], "hollowRect")
        hRectWidth = Game.WIDTH / 4 - 3
        hRectHeight = Game.HEIGHT / 2 - 3
        margin = 5
        for i in range(0, nbPlayer):
            if i == nbPlayer - 1:
                h = hollowRect((Game.WIDTH / 4) * 3, Game.HEIGHT / 2, hRectWidth, hRectHeight,
                               playerColorsList[nbPlayer-1], margin)
            else:
                h = hollowRect((Game.WIDTH / 4) * i, 0, hRectWidth, hRectHeight,
                               playerColorsList[i], margin)
            hollowRectList.l.append(h)
        return hollowRectList

    def getMyInventors(self, color):
        myparse = parse.Parse()
        myteam = myparse.getTeam()
        for team in myteam:
            if team.color == color:
                return team.inventors

    def fromRGBtoSTRINGList(self, li, size):
        returnList = []
        for i in range(0, size):
            if li[i] == Game.GREEN:
                returnList.append("green")
            elif li[i] == Game.RED:
                returnList.append("red")
            elif li[i] == Game.YELLOW:
                returnList.append("yellow")
            elif li[i] == Game.PURPLE:
                returnList.append("purple")
            elif li[i] == Game.BLUE:
                returnList.append("blue")
        return returnList

    def loadPlayerPositions(self, nbPlayer):

        positionsList = []
        for i in range(0, nbPlayer):
            if i == nbPlayer - 1:
                positionsList.append([(Game.WIDTH / 4) * 3, Game.HEIGHT / 2])
            else:
                positionsList.append([(Game.WIDTH / 4) * i, 0])
        return positionsList

    def placeInventorsNames(self, position, inventorID, nameOffset, line, name):
        lab = label(position[0] + inventorID * nameOffset + 15,
                      position[1] + 30 + line*Game.ONELINE,
                      name,
                      9)
        return lab

    def loadInventorsNames(self, nbPlayer, playerColorList, playersPositions):

        labelList = list([], "labels")

        playerColorList = self.fromRGBtoSTRINGList(playerColorList, nbPlayer)

        playerID = 0
        nameOffset = 65

        for color in playerColorList:
            inventors = self.getMyInventors(color)

            inventorId = 0

            for inventor in inventors:
                name = inventor.name.split()
                line = 0

                firstNameLabel = True

                firstNamePos = []

                for namePart in name:
                    nameLabel = self.placeInventorsNames(playersPositions[playerID],
                                                         inventorId,
                                                         nameOffset,
                                                         line,
                                                         namePart)
                    if firstNameLabel:
                        firstNameLabel = False
                        firstNamePos = [nameLabel.posX, nameLabel.posY]
                    line += 1
                    labelList.l.append(nameLabel)

                print(inventor)

                self.loadInventorsKnowledges(firstNamePos, inventor, labelList)



                inventorId += 1

            playerID += 1

        return labelList

    def loadInventorsKnowledges(self, firstNamePos, inventor, labelList):

        widthOffset = 15

        currentThenTarget = [inventor.currentKnowledge, inventor.targetKnowledge]

        for i in range(0, 2):
            heightOffset = 0
            for knowledge in currentThenTarget[i]:
                lab = label(firstNamePos[0] + i * widthOffset,
                            firstNamePos[1] + (heightOffset + 4) * Game.ONELINE,
                            str(knowledge),
                            9)
                labelList.l.append(lab)
                heightOffset += 1

    def loadGame(self, playerColor, nbPlayer):

        Game.toDisplay.clear()

        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

# Load sprites

        Game.toDisplay.append(self.loadGameSprites())

        playerColorsList = self.placePlayers(playerColor, nbPlayer)

# Load color hollow rects

        Game.toDisplay.append(self.loadGameHollowRects(nbPlayer, playerColorsList))

# Load inventorsInfos

        playersPositions = self.loadPlayerPositions(nbPlayer)
        Game.toDisplay.append(self.loadInventorsNames(nbPlayer, playerColorsList, playersPositions))

        while True:
            self.updateDisplay(Game.toDisplay, fenetre)

    def run(self):
        playerColor = self.loadSettingMenu()
        nbPlayers = self.selectIANumber(playerColor)
        self.loadGame(playerColor, nbPlayers)


myGame = Game()
myGame.run()
