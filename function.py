from data import *

class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, hp= None, image= None, speed= 5):
        super().__init__(x, y, width, height)
        self.HP = hp
        self.IMAGE = image
        self.SPPED = speed
    
class Hero(Sprite):
    def __init__(self, x, y, width, height, hp= 3, image= None, speed= 5):
        super().__init__(x, y, width, height, hp, image, speed)
        self.MOVE = {"LEFT": False, "RIGHT": False}

    def move(self, window):
        if self.MOVE["LEFT"] == True:
            self.x -= self.SPPED
        if self.MOVE["RIGHT"] == True:
            self.x += self.SPPED
        pygame.draw.rect(window, (120,120,120,),self)