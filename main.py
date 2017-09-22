#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
import pygame




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

    def showGameScreen(self):
        clock = pygame.time.Clock()
        fenetre = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        fond = pygame.image.load("background.jpg").convert()
        background = pygame.transform.scale(fond, (int(Game.WINDOW_WIDTH * 3), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(background, (0, Game.WINDOW_HEIGHT))

        fondCard = pygame.image.load("backgroundCard.png").convert()

        self.loadPlayersBackgrounds(fenetre, fondCard)

    def loadPlayersBackgrounds(self,fenetre,fondCard):
        #Display Backgrounds for players emplacements
        backgroundCard = pygame.transform.scale(fondCard, (int(Game.WINDOW_WIDTH), int(Game.WINDOW_HEIGHT)))
        fenetre.blit(backgroundCard, (0, 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*2), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*3), 0))
        fenetre.blit(backgroundCard, (int(Game.WINDOW_WIDTH*3), Game.WINDOW_HEIGHT))

        loop = True
        yellow_color = Game.YELLOW
        red_color = Game.RED
        purple_color = Game.PURPLE
        green_color = Game.GREEN
        blue_color = Game.BLUE
        white_color = Game.WHITE

        while loop:


            pygame.display.flip()
            # Draw a rectangle outline for each player area
            player1 = pygame.draw.rect(fenetre, yellow_color, [0, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            player2 = pygame.draw.rect(fenetre, red_color, [Game.WINDOW_WIDTH, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            player3 = pygame.draw.rect(fenetre, purple_color, [Game.WINDOW_WIDTH*2, 0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            player4 = pygame.draw.rect(fenetre, green_color, [Game.WINDOW_WIDTH*3,0, Game.WINDOW_WIDTH-3, Game.WINDOW_HEIGHT],
                                          5)
            player5 = pygame.draw.rect(fenetre, blue_color, [Game.WINDOW_WIDTH*3, Game.WINDOW_HEIGHT+3, Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT-5],
                                          5)
            # Draw a rectangle outline representing the gameboard with inventions cards
            board = pygame.draw.rect(fenetre,white_color,[0,Game.WINDOW_HEIGHT+5,Game.WINDOW_WIDTH*3-5,Game.WINDOW_HEIGHT-6],
                                          5)
            # retourne 1 si le curseur est au dessus du rectangle
            mouse_xy = pygame.mouse.get_pos()
            over_white = player1.collidepoint(mouse_xy)



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
        button_red =  pygame.draw.rect(fenetre, Game.RED, [Game.WIDTH/6-Game.WIDTH_BUTTON/2, Game.HEIGHT/4, Game.WIDTH_BUTTON, 50])
        button_green = pygame.draw.rect(fenetre, Game.GREEN, [Game.WIDTH/6*2-Game.WIDTH_BUTTON/2, Game.HEIGHT/4, Game.WIDTH_BUTTON, 50])
        button_blue = pygame.draw.rect(fenetre, Game.BLUE, [Game.WIDTH/6*3-Game.WIDTH_BUTTON/2, Game.HEIGHT/4,Game. WIDTH_BUTTON, 50])
        button_yellow = pygame.draw.rect(fenetre, Game.YELLOW, [Game.WIDTH/6*4-Game.WIDTH_BUTTON/2, Game.HEIGHT/4, Game.WIDTH_BUTTON, 50])
        button_purple = pygame.draw.rect(fenetre, Game.PURPLE, [Game.WIDTH/6*5-Game.WIDTH_BUTTON/2, Game.HEIGHT /4, Game.WIDTH_BUTTON, 50])

        myParse = parse.Parse()
        myColor = parse.Parse.getColor(myParse)
        for item in myColor:
            myfont = pygame.font.SysFont("monospace", 14)
            label = myfont.render(item, 1, (0, 0, 0))
            fenetre.blit(label, ((Game.WIDTH - label.get_width()) / 2, Game.HEIGHT / 5 - label.get_height()))

        myfont = pygame.font.SysFont("monospace", 52)
        # render text
        label = myfont.render("Select a player!", 1, (0, 0, 0))
        fenetre.blit(label, ((Game.WIDTH-label.get_width())/2 , Game.HEIGHT/5 -label.get_height()))
        loop = True



        while loop:

            pygame.display.flip()

            # Draw a rectangle outline representing the gameboard with inventions cards

            # retourne 1 si le curseur est au dessus du rectangle
            mouse_xy = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                # si clic, le vert devient rouge
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.showGameScreen()

            pygame.display.flip()
            # 10 fps




myGame= Game()
myGame.loadSettingMenu()



