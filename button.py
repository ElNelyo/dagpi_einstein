import pygame
from label import label


class button:

    def __init__(self, posX, posY, sizeX, sizeY, color, text, fontSize):
        self.settings = [posX, posY, sizeX, sizeY, color, text, fontSize]
        self.label = label(posX + 5, int(posY + sizeY / 2 - fontSize / 2), text, fontSize)

    def display(self, fenetre):
        posX = self.settings[0]
        posY = self.settings[1]
        sizeX = self.settings[2]
        sizeY = self.settings[3]
        color = self.settings[4]
        text = self.settings[5]
        fontSize = self.settings[6]

        pygame.draw.rect(fenetre, color, [posX, posY, sizeX, sizeY])

        self.label = label(posX + 5, int(posY + sizeY / 2 - fontSize / 2), text, fontSize)

        self.label.display(fenetre)

    def intersect(self, eventPos):
        return self.settings[0] < eventPos[0] < self.settings[0] + self.settings[2] and \
               self.settings[1] < eventPos[1] < self.settings[1] + self.settings[3]
