#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
import pygame
from list import list
from button import button
from sprite import sprite
from label import label
import random
from Gameboard import Gameboard


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
                    l.display(fenetre)

        pygame.display.flip()

    def loadSettingMenu(self):

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
                                    b.settings[5] = "test"
                                    print(b.settings[5])

    def run(self):
        self.loadSettingMenu()

myGame = Game()
myGame.run()