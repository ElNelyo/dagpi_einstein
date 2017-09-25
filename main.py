#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
import pygame
import random



class Game():
    CIEL = 0, 200, 255
    BLUE = 0, 102, 255
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    YELLOW = 255, 255, 100
    PURPLE = 204, 0, 153
    WIDTH = 1080
    HEIGHT = 720
    WINDOW_WIDTH = WIDTH / 4
    WINDOW_HEIGHT = HEIGHT / 2
    WIDTH_BUTTON = 100

    def __init__(self):
        pygame.init()

    def getMyInventors(self,colour):
        myparse = parse.Parse()
        myteam = myparse.getTeam()
        for team in myteam:
            if (team.color == colour):
                return team.inventors


    def selectIANumber(self,playerColor):
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WIDTH), int(Game.HEIGHT)))
        fenetre.blit(background, (0, 0))
        myfont = pygame.font.SysFont("monospace", 52)
        label = myfont.render("Select max numbers of players  ", 1, (0, 0, 0))
        fenetre.blit(label,((Game.WIDTH / 2-label.get_width()/2, Game.HEIGHT / 4-label.get_height())))
        loop = True
        while loop:
            button_2 = pygame.draw.rect(fenetre, Game.WHITE,
                                            [Game.WIDTH / 5 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 3, Game.WIDTH_BUTTON,
                                             50])
            button_3 = pygame.draw.rect(fenetre, Game.WHITE,
                                          [Game.WIDTH / 5 * 2 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 3, Game.WIDTH_BUTTON,
                                           50])
            button_4 = pygame.draw.rect(fenetre, Game.WHITE,
                                           [Game.WIDTH / 5 * 3 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 3, Game.WIDTH_BUTTON,
                                            50])
            button_5 = pygame.draw.rect(fenetre, Game.WHITE,
                                             [Game.WIDTH / 5 *4 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 3,
                                              Game.WIDTH_BUTTON, 50])


            for i in range(1,5):
                myfont = pygame.font.SysFont("monospace", 14)
                label = myfont.render(str(i+1), 1, (0, 0, 0))
                fenetre.blit(label, ((Game.WIDTH/5*i+label.get_width()/2,Game.HEIGHT/3)))



                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                    # si clic, le vert devient rouge

                    if event.type == pygame.MOUSEBUTTONDOWN and 0 < event.pos[0] < 250 and 150 < event.pos[1] < 250:
                        print("Players :2")
                        self.showGameScreen(playerColor,2)
                        loop = False


                    if event.type == pygame.MOUSEBUTTONDOWN and 250 < event.pos[0] < 450 and 150 < event.pos[1] < 250:
                        print("Players :3")
                        self.showGameScreen(playerColor,3)
                        loop = False


                    if event.type == pygame.MOUSEBUTTONDOWN and 450 < event.pos[0] < 700 and 150 < event.pos[1] < 250:
                        print("Players :4")
                        self.showGameScreen(playerColor,4)
                        loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN and 700 < event.pos[0] < 950 and 150 < event.pos[1] < 250:
                        print("Players :5")
                        self.showGameScreen(playerColor,5)
                        loop = False

            pygame.display.flip()







    def showGameScreen(self, playerColor,IAnumber):
        clock = pygame.time.Clock()
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WINDOW_WIDTH * 3), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(background, (0, Game.WINDOW_HEIGHT))

        fondCard = pygame.image.load("backgroundCard.png").convert()

        self.loadPlayersBackgrounds(fenetre, fondCard, playerColor)

# exchanges 2 items of a list

    def exchangeList(self, list, pos1, pos2):
        tmp = list[pos1]
        list[pos1] = list[pos2]
        list[pos2] = tmp
        return list

# Places the player in the bottom right corner and randomizes other players position

    def placeColors(self, strPlayerColor):

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

        for x in range(0, 50): # exchanges 2 positions 60 times => randomizes the list
            pos1 = 0;
            pos2 = 0;
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

        return colorList

    def loadPlayersBackgrounds(self, fenetre, fondCard, playerColor):
        #Display Backgrounds for players emplacements
        backgroundCard = pygame.transform.scale(fondCard, (int(Game.WINDOW_WIDTH), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(backgroundCard, (0, 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*2), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*3), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*3), Game.WINDOW_HEIGHT))

        loop = True

        colorList = self.placeColors(playerColor) #Place the player in the bottom right corner and
                                                    #randomize other players position

        white_color = Game.WHITE
        myplayer_inventors = self.getMyInventors(playerColor)
        fonting_space = 90
        knowledge_space = 90

        for myinventor in myplayer_inventors:
            myfont = pygame.font.SysFont("bitstreamverasans", 9)
            label = myfont.render(myinventor.name, 1, (0, 0, 0))
            fenetre.blit(label, ((Game.WIDTH-fonting_space, Game.HEIGHT-350)))
            fonting_space+=60
            for i in range(0,4):
                label = myfont.render(str(myinventor.startknowledge[i]), 1, (0, 0, 0))
                fenetre.blit(label, ((Game.WIDTH - knowledge_space, Game.HEIGHT - 350)))
                knowledge_space += 60






        while loop:


            pygame.display.flip()
            # Draw a rectangle outline for each player area

            mouse_xy = pygame.mouse.get_pos()
            player1 = pygame.draw.rect(fenetre, colorList[0], [0, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)


            player2 = pygame.draw.rect(fenetre, colorList[1], [Game.WINDOW_WIDTH, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)

            player3 = pygame.draw.rect(fenetre, colorList[2], [Game.WINDOW_WIDTH*2, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            player4 = pygame.draw.rect(fenetre, colorList[3], [Game.WINDOW_WIDTH*3,0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            myplayer = pygame.draw.rect(fenetre, colorList[4], [Game.WINDOW_WIDTH*3, Game.WINDOW_HEIGHT+3, Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT-5],
                                          5)
            # Draw a rectangle outline representing the gameboard with inventions cards
            board = pygame.draw.rect(fenetre,white_color,[0,Game.WINDOW_HEIGHT+5,Game.WINDOW_WIDTH*3-5,Game.WINDOW_HEIGHT-6],
                                          5)
            # return 1 if cursor above rectangle




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                # si clic, le vert devient rouge
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    green_color = Game.RED
                # le rectangle se cache
                elif event.type == pygame.MOUSEBUTTONDOWN and over_white:
                    white_color = Game.CIEL
                # Actualisation de l'affichage
            pygame.display.flip()
            # 10 fps

    def loadSettingMenu(self):

        clock = pygame.time.Clock()
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WIDTH), int(Game.HEIGHT)))
        fenetre.blit(background, (0, 0))


        button_green = pygame.draw.rect(fenetre, Game.GREEN, [Game.WIDTH/6-Game.WIDTH_BUTTON/2, Game.HEIGHT/4, Game.WIDTH_BUTTON, 50])
        button_red = pygame.draw.rect(fenetre, Game.RED,[Game.WIDTH / 6*4 - Game.WIDTH_BUTTON / 2, Game.HEIGHT / 4, Game.WIDTH_BUTTON, 50])
        button_blue = pygame.draw.rect(fenetre, Game.BLUE, [Game.WIDTH/6*2-Game.WIDTH_BUTTON/2, Game.HEIGHT/4,Game. WIDTH_BUTTON, 50])
        button_yellow = pygame.draw.rect(fenetre, Game.YELLOW, [Game.WIDTH/6*3-Game.WIDTH_BUTTON/2, Game.HEIGHT/4, Game.WIDTH_BUTTON, 50])
        button_purple = pygame.draw.rect(fenetre, Game.PURPLE, [Game.WIDTH/6*5-Game.WIDTH_BUTTON/2, Game.HEIGHT /4, Game.WIDTH_BUTTON, 50])

        myParse = parse.Parse()
        myColor = parse.Parse.getColor(myParse)
        fontcompt = 1

        for item in myColor:
            myfont = pygame.font.SysFont("monospace", 14)
            label = myfont.render(item, 1, (0, 0, 0))
            fenetre.blit(label, ((Game.WIDTH/6*fontcompt-Game.WIDTH_BUTTON/2+label.get_width()/2,Game.HEIGHT/4)))
            fontcompt += 1

        myfont = pygame.font.SysFont("monospace", 52)
        # render text
        label = myfont.render("Select a player!", 1, (0, 0, 0))
        fenetre.blit(label, ((Game.WIDTH-label.get_width())/2 , Game.HEIGHT/5 -label.get_height()))
        loop = True



        while loop:

            pygame.display.flip()
            mouse_xy = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    loop = False
                # si clic, le vert devient rouge

                if event.type == pygame.MOUSEBUTTONDOWN and 0 < event.pos[0] < 200 and 150 < event.pos[1] < 250:
                        print("Green team")
                        self.getMyTeam("green")
                        self.selectIANumber("green")
                        loop = False
                if event.type == pygame.MOUSEBUTTONDOWN and 200 < event.pos[0] < 400  and 150 < event.pos[1] < 250:
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

                if event.type == pygame.MOUSEBUTTONDOWN and 800 < event.pos[0] < 1000 and 150 < event.pos[1] < 250:
                        print("Purple team")
                        self.getMyTeam("purple")
                        self.selectIANumber("purple")
                        loop = False

            pygame.display.flip()
            # 10 fps

    def getMyTeam(self,colour):
        myparse = parse.Parse()
        myteams = myparse.getTeam()
        for team in myteams:

            if(team.color==colour):
                for inv in team.inventors:
                    print("Inventor added :"+inv.name)
                return team





myGame = Game()
myGame.loadSettingMenu()



