class sprite:

    def __init__(self, posX, posY, image):
        self.position = [posX, posY]
        self.image = image

    def display(self, fenetre):
        fenetre.blit(self.image, (self.position[0], self.position[1]))
