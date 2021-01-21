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

    def mainLoop(self):
        status = True

        while status:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False
                    
            pygame.display.update()





class Ship:
    def __init__(self, y, vy):
        self.y = y 
        self.vy = vy
        self.ship = pygame.image.load("resources/images/spaceship.png")




