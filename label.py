import pygame


class label:

    def __init__(self, posX, posY, text, fontSize):
        self.posX = posX
        self.posY = posY
        self.text = text
        self.fontSize = fontSize

    def display(self, fenetre):
        myfont = pygame.font.SysFont("monospace", self.fontSize)
        label = myfont.render(self.text, 1, (0, 0, 0))
        fenetre.blit(label, (self.posX, self.posY))
