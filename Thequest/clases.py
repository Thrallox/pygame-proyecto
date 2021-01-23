import pygame
from Thequest import GAME_DIMENSIONS
pygame.init()
class Game: 
    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_DIMENSIONS))
        self.background = pygame.image.load("resources/images/background.jpg")
        pygame.display.set_caption("The Quest")
        icon = pygame.image.load("resources/images/icon.png")
        pygame.display.set_icon(icon)
        self.ship = Ship(268, 0, 10)
        
    def mainLoop(self):
        status = True
        while status:
            self.screen.blit(self.background,(0,0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False

                self.ship.eventHandler(event)

            self.ship.yUpdate()
            self.screen.blit(self.ship.disfraz, (self.ship.x,self.ship.y))  
                    
            pygame.display.update()



class Ship:
    def __init__(self, y, vy, x):
        self.y = y 
        self.vy = vy
        self.x = x
        self.disfraz = pygame.image.load("resources/images/spaceship.png")

    
    
    def eventHandler(self,event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.vy = -0.5
        
            if event.key == pygame.K_DOWN:
                self.vy = 0.5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.vy =  0

    def yUpdate(self): 
        self.y += self.vy

        if self.y <= 0:
            self.y = 0
        elif self.y >= 568:
            self.y = 568
    




