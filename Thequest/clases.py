import pygame
from Thequest import GAME_DIMENSIONS, FPS
pygame.init()
class Game: 
    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_DIMENSIONS))
        self.background = pygame.image.load("resources/images/fondo1.jpg")
        self.bgMainMenu = pygame.image.load("resources/images/mainmenu.jpg")  
        pygame.display.set_caption("The Quest")
        icon = pygame.image.load("resources/images/icon.png")
        pygame.display.set_icon(icon)
        self.ship = Ship(268, 5, 10)
        self.clock = pygame.time.Clock()

    

    def mainMenu(self):
        mainMenu = True
        x=0
        ix=0
        ciclosRefresco=0
        retardoAnimacion = 20
        while mainMenu:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mainLoop()
                        

            #Movimiento del manu principal
            rel_x = x % self.bgMainMenu.get_rect().width
            self.screen.blit(self.bgMainMenu, (rel_x - self.bgMainMenu.get_rect().width,0))
            if rel_x <= GAME_DIMENSIONS[0]:
                self.screen.blit(self.bgMainMenu, (rel_x,0))
            x -=1
            #Se define el titulo 
            name = pygame.font.Font("resources/titulo.ttf", 90)
            name_img = name.render("THE QUEST",False,(255,179,102))
            self.screen.blit(name_img,(100,250))
            #Se pone el mensaje de barra espaciadora 
            colores =[(0,255,0), (255,255,255)]
            tecla_espacio = pygame.font.Font("resources/espacio.ttf",25)
            tecla_espacio_img = tecla_espacio.render("Press <SPACE BAR> in order to continue", False, colores[ix])
            ciclosRefresco +=1
            if ciclosRefresco == retardoAnimacion:
                if ix == 0:
                    ix = 1
                else:
                    ix = 0
                
                ciclosRefresco = 0
                
            self.screen.blit(tecla_espacio_img, (110,450))
                            
            pygame.display.update()

    def mainLoop(self):
        x=0
        status = True
        while status:
            self.clock.tick(FPS)
            self.screen.blit(self.background,(0,0))
            rel_x = x % self.background.get_rect().width
            self.screen.blit(self.background, (rel_x - self.background.get_rect().width,0))
            if rel_x <= GAME_DIMENSIONS[0]:
                self.screen.blit(self.background, (rel_x,0))
            x -=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False

                self.ship.eventHandler(event)

            self.ship.yUpdate()
            self.screen.blit(self.ship.disfraz, (self.ship.x,self.ship.y))  
                    
            pygame.display.update()


class Ship:
    def __init__(self, y, velocidad, x):
        self.y = y 
        self.vy = 0
        self.velocidad = velocidad
        self.neutro = 0
        self.x = x
        self.disfraz = pygame.image.load("resources/images/spaceship.png")

    def eventHandler(self,event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.vy = -self.velocidad
        
            if event.key == pygame.K_DOWN:
                self.vy = self.velocidad
            '''    
            if event.key == pygame.K_UP and event.key == pygame.K_DOWN:
                self.vy = self.velocidad

            if event.key == pygame.K_DOWN and event.key == pygame.K_UP:
                self.vy = -self.velocidad
            '''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.vy =  self.neutro
        
    def yUpdate(self): 
        self.y += self.vy

        if self.y <= 0:
            self.y = 0
        elif self.y >= 568:
            self.y = 568
    





