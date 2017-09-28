import pygame

class hollowRect:

    def __init__(self, posX, posY, sizeX, sizeY, color, margin):
        self.settings = [posX, posY, sizeX, sizeY, color, margin]

    def display(self, fenetre):
        posX = self.settings[0]
        posY = self.settings[1]
        sizeX = self.settings[2]
        sizeY = self.settings[3]
        color = self.settings[4]
        margin = self.settings[5]

        pygame.draw.rect(fenetre, color, [posX, posY, sizeX, sizeY], margin)
