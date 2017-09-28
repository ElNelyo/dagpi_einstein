#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from function import Function
import pygame
import Player
import parse
from Gameboard import Gameboard


class Game():
    CIEL = 0, 200, 255
    BLUE = 0, 102, 255
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    YELLOW = 255, 255, 100
    PURPLE = 204, 0, 153
    GRAY = 150, 150, 150
    WIDTH = 1080
    HEIGHT = 720
    WINDOW_WIDTH = WIDTH / 4
    WINDOW_HEIGHT = HEIGHT / 2
    WIDTH_BUTTON = 100

    def __init__(self):
        pygame.init()

    def setLeonardo(self, player, fenetre):
        leonardo = "Leonardo : " + player
        myfont = pygame.font.SysFont("monospace", 12)
        label = myfont.render(leonardo, 1, (0, 0, 0))
        fenetre.blit(label, (540, 375))

    def getMyInventors(self, colour):
        myparse = parse.Parse()
        myteam = myparse.getTeam()
        for team in myteam:
            if (team.color == colour):
                return team.inventors

    def drawButtonNbPlayer(self, fenetre, offset):
        return pygame.draw.rect(fenetre, Game.WHITE,
                                [Game.WIDTH / 5 * offset - Game.WIDTH_BUTTON / 2,
                                 Game.HEIGHT / 3, Game.WIDTH_BUTTON, 50])

    def selectIALevel(self):
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WIDTH), int(Game.HEIGHT)))
        fenetre.blit(background, (0, 0))
        myfont = pygame.font.SysFont("monospace", 52)
        label = myfont.render("Select the difficulty", 1, (0, 0, 0))
        fenetre.blit(label, (Game.WIDTH / 2 - label.get_width() / 2, Game.HEIGHT / 4 - label.get_height()))

        button_IABasic = pygame.draw.rect(fenetre, Game.WHITE,
                                          [Game.WIDTH / 5, Game.HEIGHT / 3, Game.WIDTH_BUTTON, 50])
        button_IAAdvanced = pygame.draw.rect(fenetre, Game.WHITE,
                                             [Game.WIDTH / 5 * 4, Game.HEIGHT / 3, Game.WIDTH_BUTTON, 50])

        myfont = pygame.font.SysFont("monospace", 12)
        labelAI1 = myfont.render(str("AI Basic"), 1, (0, 0, 0))
        labelAI2 = myfont.render(str("AI Advanced"), 1, (0, 0, 0))
        fenetre.blit(labelAI1, (Game.WIDTH / 5 + 10, Game.HEIGHT / 3 + 20))
        fenetre.blit(labelAI2, (Game.WIDTH / 5 * 4 + 10, Game.HEIGHT / 3 + 20))

        pygame.display.flip()
        loop = True
        while loop:

            for i in range(1, 5):
                myfont = pygame.font.SysFont("monospace", 14)
                # label = myfont.render(str(i + 1), 1, (0, 0, 0))
                fenetre.blit(label, (Game.WIDTH / 2 - label.get_width() / 2, Game.HEIGHT / 4 - label.get_height()))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continue

                    if event.type == pygame.MOUSEBUTTONDOWN and Game.WIDTH / 5 < event.pos[
                        0] < Game.WIDTH / 5 + Game.WIDTH_BUTTON and Game.HEIGHT / 3 < event.pos[
                        1] < Game.HEIGHT / 3 + 50:
                        print("AI Basic")
                        self.loadSettingMenu()
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and Game.WIDTH / 5 * 4 < event.pos[
                        0] < Game.WIDTH / 5 * 4 + Game.WIDTH_BUTTON and Game.HEIGHT / 3 < event.pos[
                        1] < Game.HEIGHT / 3 + 50:
                        print("AI Advanced")
                        self.loadSettingMenu()
                        loop = False
            pygame.display.flip()

    def selectIANumber(self, playerColor):
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WIDTH), int(Game.HEIGHT)))
        fenetre.blit(background, (0, 0))
        myfont = pygame.font.SysFont("monospace", 52)
        label = myfont.render("Select max numbers of players  ", 1, (0, 0, 0))
        fenetre.blit(label, (Game.WIDTH / 2 - label.get_width() / 2, Game.HEIGHT / 4 - label.get_height()))

        loop = True

        while loop:

            button_2 = self.drawButtonNbPlayer(fenetre, 1)
            button_3 = self.drawButtonNbPlayer(fenetre, 2)
            button_4 = self.drawButtonNbPlayer(fenetre, 3)
            button_5 = self.drawButtonNbPlayer(fenetre, 4)

            for i in range(1, 5):
                myfont = pygame.font.SysFont("monospace", 14)
                label = myfont.render(str(i + 1), 1, (0, 0, 0))
                fenetre.blit(label, (Game.WIDTH / 5 * i + label.get_width() / 2, Game.HEIGHT / 3))

                nbPlayer = 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and 166 < event.pos[0] < 266 and 240 < event.pos[1] < 290:
                        print("Players :2")
                        self.showGameScreen(playerColor, 2)
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and 382 < event.pos[0] < 482 and 240 < event.pos[1] < 290:
                        print("Players :3")
                        self.showGameScreen(playerColor, 3)
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and 598 < event.pos[0] < 698 and 240 < event.pos[1] < 290:
                        print("Players :4")
                        self.showGameScreen(playerColor, 4)
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and 814 < event.pos[0] < 914 and 240 < event.pos[1] < 290:
                        print("Players :5")
                        self.showGameScreen(playerColor, 5)
                        loop = False

            pygame.display.flip()

    def showGameScreen(self, playerColor, IAnumber):
        clock = pygame.time.Clock()
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WINDOW_WIDTH * 3), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(background, (0, Game.WINDOW_HEIGHT))

        fondCard = pygame.image.load("backgroundCard.png").convert()
        self.setLeonardo("null", fenetre)
        self.loadPlayersBackgrounds(fenetre, fondCard, playerColor, IAnumber)

    # exchanges 2 items of a list

    def exchangeList(self, list, pos1, pos2):
        tmp = list[pos1]
        list[pos1] = list[pos2]
        list[pos2] = tmp
        return list

    # Places the player in the bottom right corner and randomizes other players position

    def placeColors(self, strPlayerColor, IANumber):

        if strPlayerColor == "green":
            playerColor = Game.GREEN
        elif strPlayerColor == "purple":
            playerColor = Game.PURPLE
        elif strPlayerColor == "red":
            playerColor = Game.RED
        elif strPlayerColor == "yellow":
            playerColor = Game.YELLOW
        elif strPlayerColor == "blue":
            playerColor = Game.BLUE

        colorList = [Game.PURPLE, Game.YELLOW, Game.GREEN, Game.BLUE, Game.RED]

        # exchanges 2 positions 60 times => randomizes the list

        for x in range(0, 50):
            pos1 = 0
            pos2 = 0
            while pos1 == pos2:
                pos1 = random.randrange(0, 5, 1)
                pos2 = random.randrange(0, 5, 1)
            colorList = self.exchangeList(colorList, pos1, pos2)

        pos = 0
        for x in range(0, 5):
            if colorList[x] == playerColor:
                pos = x

        if pos != 4:
            colorList = self.exchangeList(colorList, pos, 4)

        for i in range(0, 5 - IANumber):
            colorList.pop(0)

        return colorList

    def fromRGBtoSTRINGList(self, list, size):
        returnList = []
        for i in range(0, size):
            if list[i] == Game.GREEN:
                returnList.append("green")
            elif list[i] == Game.RED:
                returnList.append("red")
            elif list[i] == Game.YELLOW:
                returnList.append("yellow")
            elif list[i] == Game.PURPLE:
                returnList.append("purple")
            elif list[i] == Game.BLUE:
                returnList.append("blue")
        return returnList

    def displayKnowledge(self, myfont, knowledge, fenetre, pos1, pos2):
        label = myfont.render(knowledge, 1, (0, 0, 0))
        fenetre.blit(label, (pos1, pos2))

    def displayInventors(self, intPlayer, colorListString, originPosition, fenetre):

        oneLine = 12
        fonting_space = 40
        knowledge_space = 90
        inventors = self.getMyInventors(colorListString[intPlayer])
        namePos = [originPosition[0] + fonting_space, originPosition[1] + 30]

        myfont = pygame.font.SysFont("bitstreamverasans", 10)
        label1 = myfont.render(str("Age1"), 1, (0, 0, 0))
        label2 = myfont.render(str("Age2"), 1, (0, 0, 0))
        label3 = myfont.render(str("Age3"), 1, (0, 0, 0))
        fenetre.blit(label1, (830, 550))
        fenetre.blit(label2, (870, 550))
        fenetre.blit(label3, (910, 550))

        myfont = pygame.font.SysFont("bitstreamverasans", 12)

        knowledgeLegend = ["Ph :", "Ch :", "Me :", "Ma :", "Vpt :"]

        toAddToI = 5

        for i in range(0, 5):  # display the legend

            label = myfont.render(knowledgeLegend[i], 1, (0, 0, 0))
            if i == 4:
                toAddToI = 6
            fenetre.blit(label, (namePos[0] - 30, namePos[1] + (toAddToI + i) * oneLine))

        myfont = pygame.font.SysFont("bitstreamverasans", 9)

        ownedcard = [["Age1", [namePos[0], -150 + namePos[1] * oneLine]],
                     ["Age2", [namePos[0] + 30, -150 + namePos[1] * oneLine]],
                     ["Age3", [namePos[0] + 60, -150 + namePos[1] * oneLine]]]

        for card in ownedcard:
            label = myfont.render(card[0], 1, (0, 0, 0))
            fenetre.blit(label, card[1])

        for inventor in inventors:

            namePos = [originPosition[0] + fonting_space, originPosition[1] + 30]

            # separates fist and last name into a list

            name = inventor.name.split()

            vPoints = inventor.points

            myfont = pygame.font.SysFont("bitstreamverasans", 9)

            label1 = myfont.render(name[0], 1, (0, 0, 0))
            if len(name) > 1:
                label2 = myfont.render(name[1], 1, (0, 0, 0))
            if len(name) > 2:
                label3 = myfont.render(name[2], 1, (0, 0, 0))

            if len(name) > 0:
                fenetre.blit(label1, (namePos[0], namePos[1]))
            if len(name) > 1:
                fenetre.blit(label2, (namePos[0], namePos[1] + oneLine))
            if len(name) > 2:
                fenetre.blit(label3, (namePos[0], namePos[1] + oneLine * 2))

            fonting_space += 61

            myfont = pygame.font.SysFont("bitstreamverasans", 9)

            startTargetLegend = [["CP", [namePos[0], namePos[1] + 4 * oneLine]],
                                 ["TP", [namePos[0] + 20, namePos[1] + 4 * oneLine]]]

            for legend in startTargetLegend:
                label = myfont.render(legend[0], 1, (0, 0, 0))
                fenetre.blit(label, legend[1])

            for i in range(0, 4):
                self.displayKnowledge(myfont, str(inventor.currentKnowledge[i]),
                                      fenetre, namePos[0], namePos[1] + (5 + i) * 12)
                self.displayKnowledge(myfont, str(inventor.targetKnowledge[i]),
                                      fenetre, namePos[0] + 20, namePos[1] + (5 + i) * 12)

            label = myfont.render(vPoints, 1, (0, 0, 0))
            fenetre.blit(label, (namePos[0], namePos[1] + (7 + i) * oneLine))

    def displayToken(self, fenetre):

        line = 2
        height = int(self.HEIGHT / 4)  # 1/4 of the screen height
        tokenOnBoard = self.gameboard.emplacementOnBoard
        myfonttoken = pygame.font.SysFont("bitstreamverasans", 10)

        i = 0
        for token in tokenOnBoard:
            print(token[1].type)
            if i > 3:
                line = 3

            if token[1].type == "pointReward":
                token1 = myfonttoken.render(str("PT" + str(token[1].level)), 1, (0, 0, 0))
                fenetre.blit(token1, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[2].type == "pointReward":
                token2 = myfonttoken.render(str("PT" + str(token[2].level)), 1, (0, 0, 0))
                fenetre.blit(token2, (80 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[1].type == "progressReward":
                token1 = myfonttoken.render(str("P" + str(token[1].level)), 1, (0, 0, 0))
                fenetre.blit(token1, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[2].type == "progressReward":
                token2 = myfonttoken.render(str("P" + str(token[2].level)), 1, (0, 0, 0))
                fenetre.blit(token2, (80 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[1].type == "availabilityReward":
                token1 = myfonttoken.render("CF", 1, (0, 0, 0))
                fenetre.blit(token1, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))
            if token[2].type == "availabilityReward":
                token2 = myfonttoken.render("CF", 1, (0, 0, 0))
                fenetre.blit(token2, (80 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[1].type == "additonalKnowledgeReward":
                token1 = myfonttoken.render("DG", 1, (0, 0, 0))
                fenetre.blit(token1, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))
            if token[2].type == "additonalKnowledgeReward":
                token2 = myfonttoken.render("DG", 1, (0, 0, 0))
                fenetre.blit(token2, (80 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            if token[1].type == "classificationReward":
                token1 = myfonttoken.render("ST", 1, (0, 0, 0))
                fenetre.blit(token1, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))
            if token[2].type == "classificationReward":
                token2 = myfonttoken.render("ST", 1, (0, 0, 0))
                fenetre.blit(token2, (80 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

            i += 1

    def displayCards(self, cards, fenetre):

        rectSize = 16
        positions = []
        myfont = pygame.font.SysFont("bitstreamverasans", 10)
        line = 2
        height = int(self.HEIGHT / 4)  # 1/4 of the screen height

        height = int(self.HEIGHT / 4)  # 1/4 of the screen height

        for i in range(0, len(cards)):
            if i > 3:
                line = 3
            positions.append([int(30 + int(i % 4) * (self.WIDTH / 8)), line * height + 30])
            label = myfont.render(cards[i].name, 1, (0, 0, 0))
            classicationlabel = myfont.render(str(cards[i].classification), 1, (0, 0, 0))

            fenetre.blit(label, (30 + int((i % 4) * (self.WIDTH / 8)), line * height + 30))
            fenetre.blit(classicationlabel, (15 + int((i % 4) * (self.WIDTH / 8)), line * height + 130))

        myfont = pygame.font.SysFont("bitstreamverasans", 14)
        knowledgeLegend = ["Ph :", "Ch :", "Me :", "Ma :"]

        for i in range(0, len(cards)):
            heightoffest = 20
            heightknow = 5
            currentCard = cards[i]

            knId = 0

            for kn in currentCard.knowledge:
                widthoffset = 0

                for j in range(0, kn):
                    pygame.draw.rect(fenetre, currentCard.generalKnowledgeColors[knId][j],
                                     [positions[i][0] + widthoffset, positions[i][1] + heightoffest,
                                      rectSize, rectSize])
                    widthoffset += (rectSize + 2)

                heightoffest += (rectSize + 2)
                knId += 1
            if i > 4:
                for i in range(0, 4):
                    heightknow = 20
                    for j in range(0, 4):
                        myfont = pygame.font.SysFont("monospace", 12)
                        label = myfont.render(knowledgeLegend[j], 1, (0, 0, 0))
                        fenetre.blit(label, (positions[i][0] - 25, positions[i][1] + heightknow))
                        heightknow += 19
            else:
                for i in range(i, len(cards) - 4):
                    heightknow = 20
                    for j in range(0, 4):
                        myfont = pygame.font.SysFont("monospace", 12)
                        label = myfont.render(knowledgeLegend[j], 1, (0, 0, 0))
                        fenetre.blit(label, (positions[i][0] - 25, positions[i][1] + heightknow + 178))
                        heightknow += 19

    def displayButton(self, fenetre, text, posX, posY, sizeX, sizeY, fontSize, color):

        buttonSettings = [posX, posY, sizeX, sizeY]

        pygame.draw.rect(fenetre, color, [posX, posY, sizeX, sizeY])

        myfont = pygame.font.SysFont("bitstreamverasans", fontSize)
        label = myfont.render(text, 1, (0, 0, 0))

        fenetre.blit(label, (posX + 5, int(posY + sizeY / 2 - fontSize / 2)))

        return buttonSettings

    def overButton(self, eventPos, buttonSettings):
        return buttonSettings[0] < eventPos[0] < buttonSettings[0] + buttonSettings[2] and \
               buttonSettings[1] < eventPos[1] < buttonSettings[1] + buttonSettings[3]

    def displayDropList(self, fenetre, buttonSettings, inventors):
        offsetX = buttonSettings[2] + 1
        offsetY = buttonSettings[3]
        oneLine = 0
        boutons = []
        color = Game.WHITE
        for inventor in inventors:
            if inventor.sleep:
                color = Game.GRAY
            else:
                color = Game.WHITE
            self.displayButton(fenetre, inventor.name, buttonSettings[0] + offsetX,
                               buttonSettings[1] + oneLine,
                               110, 15, 10, color)
            boutons.append([buttonSettings[0] + offsetX, buttonSettings[1] + oneLine, 100, 15])
            oneLine += 16

        return boutons

    def displayInventionPossible(self, fenetre, buttonSettings, inventions):
        offsetX = buttonSettings[2] + 1
        offsetY = buttonSettings[3]
        oneLine = 0
        boutons = []
        color = Game.WHITE
        for invention in inventions:
            color = Game.WHITE
            self.displayButton(fenetre, invention[2].name, buttonSettings[0] + offsetX,
                               buttonSettings[1] + oneLine,
                               110, 15, 10, color)
            boutons.append([buttonSettings[0] + offsetX, buttonSettings[1] + oneLine, 100, 15, invention[2].name])
            oneLine += 16

        return boutons

    def fromStringToRGB(self, strColor):

        if strColor == "green":
            return Game.GREEN
        elif strColor == "purple":
            return Game.PURPLE
        elif strColor == "red":
            return Game.RED
        elif strColor == "yellow":
            return Game.YELLOW
        elif strColor == "blue":
            return Game.BLUE

    def placeCube(self, playerColor, cards, inventionClicked, clickedInventor, fenetre):

        RGBPlayerColor = self.fromStringToRGB(playerColor)

        # Here if clicked on an invention in the dropList to add cubes on it

        # We have inventionClicked and clickedInventor

        knId = 0
        for knowledge in clickedInventor.currentKnowledge:
            for i in range(0, knowledge):

                colorsToTest = inventionClicked.generalKnowledgeColors[knId]

                placeCubeLoop = True
                position = 0

                if len(colorsToTest) > 0:
                    while position < (len(colorsToTest)) and placeCubeLoop:
                        print(knId, " ", position)
                        if colorsToTest[position] == Game.WHITE:
                            placeCubeLoop = False
                            colorsToTest[position] = RGBPlayerColor
                        position += 1

            knId += 1

        self.displayCards(cards, fenetre)

        pygame.display.flip()

    def loadPlayersBackgrounds(self, fenetre, fondCard, playerColor, IANumber):

        dropListDisplayed = False
        dropListActionDisplayed = False
        myInventors = self.getMyInventors(playerColor)
        inventorName = ""
        ActionChoosen = []
        InventorChoosen = []
        hasChoosenAction = False
        CubePosed = False

        # Display Backgrounds for players emplacements
        backgroundCard = pygame.transform.scale(fondCard, (int(Game.WINDOW_WIDTH), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(backgroundCard, (0, 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH * 2), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH * 3), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH * 3), Game.WINDOW_HEIGHT))

        playerPositions = [[0, 0]]
        if IANumber > 2:
            playerPositions.append([int(Game.WINDOW_WIDTH), 0])
        if IANumber > 3:
            playerPositions.append([int(Game.WINDOW_WIDTH * 2), 0])
        if IANumber > 4:
            playerPositions.append([int(Game.WINDOW_WIDTH * 3), 0])
        playerPositions.append([int(Game.WINDOW_WIDTH * 3), int(Game.WINDOW_HEIGHT)])

        loop = True

        colorList = self.placeColors(playerColor, IANumber)  # Place the player in the bottom right corner and
        # randomize other players position

        white_color = Game.WHITE

        colorListString = self.fromRGBtoSTRINGList(colorList, len(colorList))
        listPlayer = []
        for color in colorListString:
            player = Player.Player("Player", False)
            player.chooseTeam(color)
            listPlayer.append(player)

        # Display the inventors infos
        self.gameboard = Gameboard(1, listPlayer)
        cards = self.gameboard.distribute()
        self.gameboard.newTurn()
        for player in range(0, IANumber):
            self.displayInventors(player, colorListString, playerPositions[player], fenetre)
        self.displayToken(fenetre)
        self.displayCards(cards, fenetre)

        # Top Button
        button1Settings = self.displayButton(fenetre, "PlaceCube",
                                             Game.WIDTH / 2, Game.HEIGHT / 2 + 30, 100, 50, 14, Game.WHITE)
        buttonAddKnowledge = self.displayButton(fenetre, "Add knowledge",
                                                Game.WIDTH / 2, Game.HEIGHT / 10 * 7 + 30, 100, 50, 14, Game.WHITE)

        # Bottom Buttons
        buttonCoffee = self.displayButton(fenetre, "Coffee",
                                          Game.WIDTH / 2, Game.HEIGHT / 10 * 9 + 30, 60, 20, 14, Game.WHITE)
        buttonRecycle = self.displayButton(fenetre, "Recycle",
                                           Game.WINDOW_WIDTH * 2 + Game.WINDOW_WIDTH / 3, Game.HEIGHT / 10 * 9 + 30, 60,
                                           20, 14, Game.WHITE)

        while loop:

            inventionClicked = 0

            pygame.display.flip()
            # Draw a rectangle outline for each player area

            mouse_xy = pygame.mouse.get_pos()

            player1 = pygame.draw.rect(fenetre, colorList[0], [0, 0, Game.WINDOW_WIDTH - 3, Game.WINDOW_HEIGHT],
                                       5)
            if IANumber > 2:
                player2 = pygame.draw.rect(fenetre, colorList[1],
                                           [Game.WINDOW_WIDTH, 0, Game.WINDOW_WIDTH - 3, Game.WINDOW_HEIGHT],
                                           5)

            if IANumber > 3:
                player3 = pygame.draw.rect(fenetre, colorList[2],
                                           [Game.WINDOW_WIDTH * 2, 0, Game.WINDOW_WIDTH - 3, Game.WINDOW_HEIGHT],
                                           5)

            if IANumber > 4:
                player4 = pygame.draw.rect(fenetre, colorList[3],
                                           [Game.WINDOW_WIDTH * 3, 0, Game.WINDOW_WIDTH - 3, Game.WINDOW_HEIGHT],
                                           5)

            myplayer = pygame.draw.rect(fenetre, colorList[IANumber - 1],
                                        [Game.WINDOW_WIDTH * 3, Game.WINDOW_HEIGHT + 3, Game.WINDOW_WIDTH,
                                         Game.WINDOW_HEIGHT - 5],
                                        5)

            # Draw a rectangle outline representing the gameboard with inventions cards
            board = pygame.draw.rect(fenetre, white_color,
                                     [0, Game.WINDOW_HEIGHT + 5, Game.WINDOW_WIDTH * 3 - 5, Game.WINDOW_HEIGHT - 6],
                                     5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                elif event.type == pygame.MOUSEBUTTONDOWN and dropListActionDisplayed:
                    droplistAction = self.displayInventionPossible(fenetre, button1Settings, inventionListPosssible)
                    for button in droplistAction:
                        if self.overButton(event.pos, button):

                            for invention in cards:
                                if invention.name == button[4]:  # If invention name is the same as button label
                                    inventionClicked = invention

                            self.placeCube(playerColor, cards, inventionClicked, clickedInventor, fenetre)

                            clickedInventor.sleep = True

                            # We have played, time for the random AIs

                            for AI in colorListString:
                                
                                if(AI != playerColor):
                                    intors = self.getMyInventors(AI)
                                    ID = random.randrange(0, 4)
                                    intor = intors[ID]

                                    inventionList = intor.boardCardsForInventor(cards)
                                    if len(inventionList) > 0:
                                        ID = random.randrange(0, len(inventionList))
                                        intion = inventionList[ID]
                                        self.placeCube(AI, cards, intion, intor, fenetre)
                                    else:
                                        team = self.getMyTeam(AI)
                                        for inventor in team.inventors:
                                            inventor.sleep = False
                                        print("Player ", AI, " recycles !")


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.overButton(event.pos, button1Settings):
                        if dropListDisplayed:
                            print("hide droplist")  # TODO
                        else:
                            dropList = self.displayDropList(fenetre, button1Settings, myInventors)
                        dropListDisplayed = not dropListDisplayed
                    inventionListPosssible = []
                    if dropListDisplayed:
                        for button in dropList:
                            if self.overButton(event.pos, button):
                                clickedInventor = self.gameboard.playersOnBoard[len(self.gameboard.playersOnBoard)-1].myTeam.inventors[int((button[1] - 390) / 16)]
                                clickedInventor.sleep = True
                                dropList = self.displayDropList(fenetre, button1Settings, myInventors)
                                print(clickedInventor.name)
                                InventorChoosen.append(clickedInventor)
                                dropListDisplayed = not dropListDisplayed
                                for action in self.gameboard.possibleactions:
                                    dropListDisplayed = False

                                    if action[1].name == clickedInventor.name:

                                        inventionListPosssible.append(action)
                                        dropListActionDisplayed = not dropListActionDisplayed

                                dropListActionDisplayed = True

                    if event.type == pygame.MOUSEBUTTONDOWN and hasChoosenAction and  Game.WIDTH / 2 + 180 < event.pos[
                                    0] < Game.WIDTH / 2 + 250 and Game.HEIGHT / 10 * 9 + 30 < event.pos[
                                    1] < Game.HEIGHT / 10 * 9 + 50:

                        print(ActionChoosen)

                                # Click on Coffee button
                    if event.type == pygame.MOUSEBUTTONDOWN and Game.WIDTH / 2 < event.pos[
                        0] < Game.WIDTH / 2 + 60 and Game.HEIGHT / 10 * 9 + 30 < event.pos[
                        1] < Game.HEIGHT / 10 * 9 + 50:
                        loopToken = True
                        while loopToken:
                            print(self.gameboard.playersOnBoard[self.gameboard.currentPlayer].myTeam.listTokens)
                            for token in self.gameboard.playersOnBoard[self.gameboard.currentPlayer].myTeam.listTokens:
                                # If the tokenList contain an availabilityReward then it remove this one, and call the awake function on all inventors
                                # Then, it leave the loop
                                if token.type == "availabilityReward":
                                    self.gameboard.playersOnBoard[self.gameboard.currentPlayer].myTeam.listTokens.remove(token)
                                    self.gameboard.awakeCurrentPlayer()
                                    break
                            loopToken = False

                    #         Recycle button
                    if event.type == pygame.MOUSEBUTTONDOWN and Game.WINDOW_WIDTH * 2 + Game.WINDOW_WIDTH / 3 < event.pos[
                        0] < Game.WINDOW_WIDTH * 2 + Game.WINDOW_WIDTH / 3 + 60 and Game.HEIGHT / 10 * 9 + 30 < event.pos[
                        1] < Game.HEIGHT / 10 * 9 + 50:
                        self.gameboard.awakeCurrentPlayer()
                        self.gameboard.newTurn()
                        print("Recycle button yata ! ")

            pygame.display.flip()
            # 10 fps

    def loadSettingMenu(self):

        clock = pygame.time.Clock()
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WIDTH), int(Game.HEIGHT)))
        fenetre.blit(background, (0, 0))

        button_green = pygame.draw.rect(fenetre, Game.GREEN,
                                        [Game.WIDTH / 6 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4, Game.WIDTH_BUTTON,
                                         50])
        button_red = pygame.draw.rect(fenetre, Game.RED,
                                      [Game.WIDTH / 6 * 4 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4, Game.WIDTH_BUTTON,
                                       50])
        button_blue = pygame.draw.rect(fenetre, Game.BLUE,
                                       [Game.WIDTH / 6 * 2 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4, Game.WIDTH_BUTTON,
                                        50])
        button_yellow = pygame.draw.rect(fenetre, Game.YELLOW,
                                         [Game.WIDTH / 6 * 3 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4,
                                          Game.WIDTH_BUTTON, 50])
        button_purple = pygame.draw.rect(fenetre, Game.PURPLE,
                                         [Game.WIDTH / 6 * 5 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4,
                                          Game.WIDTH_BUTTON, 50])

        myParse = parse.Parse()
        myColor = parse.Parse.getColor(myParse)
        fontcompt = 1

        for item in myColor:
            myfont = pygame.font.SysFont("monospace", 14)
            label = myfont.render(item, 1, (0, 0, 0))
            fenetre.blit(label, (
                (Game.WIDTH / 6 * fontcompt - Game.WIDTH_BUTTON / 2 + label.get_width() / 2, Game.HEIGHT / 4)))
            fontcompt += 1

        myfont = pygame.font.SysFont("monospace", 52)
        # render text
        label = myfont.render("Select a player!", 1, (0, 0, 0))
        fenetre.blit(label, ((Game.WIDTH - label.get_width()) / 2, Game.HEIGHT / 5 - label.get_height()))
        loop = True

        while loop:

            pygame.display.flip()
            mouse_xy = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN and 0 < event.pos[0] < 200 and 150 < event.pos[1] < 250:
                    print("Green team")
                    self.getMyTeam("green")
                    self.selectIANumber("green")
                    loop = False
                if event.type == pygame.MOUSEBUTTONDOWN and 200 < event.pos[0] < 400 and 150 < event.pos[1] < 250:
                    print("Blue team")
                    self.getMyTeam("blue")
                    self.selectIANumber("blue")
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN and 400 < event.pos[0] < 600 and 150 < event.pos[1] < 250:
                    print("Yellow team")
                    self.getMyTeam("yellow")
                    self.selectIANumber("yellow")
                    loop = False
                if event.type == pygame.MOUSEBUTTONDOWN and 600 < event.pos[0] < 800 and 150 < event.pos[1] < 250:
                    print("Red team")
                    self.getMyTeam("red")
                    self.selectIANumber("red")
                    loop = False

                if event.type == pygame.MOUSEBUTTONDOWN and 800 < event.pos[0] < 1000 and 150 < event.pos[1] < 250:
                    print("Purple team")
                    self.getMyTeam("purple")
                    self.selectIANumber("purple")
                    loop = False

            pygame.display.flip()
            # 10 fps

    def getMyTeam(self, colour):
        myparse = parse.Parse()
        myteams = myparse.getTeam()
        for team in myteams:

            if team.color == colour:
                for inv in team.inventors:
                    print("Inventor added :" + inv.name)
                return team

    def Next(self, Invention, Inventor):
        knowledgeposed = []
        for i in range (0,3):
            if Inventor[0].currentKnowledge[i] !=0:
                knowledgeposed.append(Inventor[0].name)
                knowledgeposed.append(Inventor[0].currentKnowledge[i])
            Invention.knowledgeposed = knowledgeposed
        #print(Invention.knowledge)
        #print(Inventor[0].currentKnowledge)



myGame = Game()
myGame.selectIALevel()
