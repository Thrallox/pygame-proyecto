import pygame
from Thequest import GAME_DIMENSIONS, FPS
from pygame import mixer
import random
pygame.init()
class Game: 
    def __init__(self):
        self.screen = pygame.display.set_mode((GAME_DIMENSIONS))
        self.background = pygame.image.load("resources/images/fondo1.jpg")
        self.bgMainMenu = pygame.image.load("resources/images/mainmenu.jpg")  
        pygame.display.set_caption("The Quest")
        icon = pygame.image.load("resources/images/icon.png")
        pygame.display.set_icon(icon)
        self.ship = Ship(268,7, 10)
        self.planeta1 = Planeta(730,-90,10)
        self.clock = pygame.time.Clock()
        self.obstaculos = []

    
        for i in range (random.randint(5,10)):
            obstaculo = Obstaculo()
            self.obstaculos.append(obstaculo)
            for obstaculo in self.obstaculos:
                obstaculo.obstacleUpdate()
        

    def pintaObstaculo(self):
        for obstaculo in self.obstaculos:
            self.screen.blit (obstaculo.asteroid, (obstaculo.x, obstaculo.y))


    def pintaPlaneta(self):
            self.screen.blit(self.planeta1.planeta_img,(self.planeta1.x,self.planeta1.y))
            if self.planeta1.x ==550:
                self.planeta1.x =550
            else:
                self.planeta1.x -=1


    def mission(self):
        sonidoMision = mixer.Sound("resources/missionMenu.wav")
        sonidoMision.play(-1)
        sonidoMision.set_volume(0.2)
        notReady = True
        ix=0
        ciclosRefresco=0
        retardoAnimacion = 25
        while notReady:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    notReady = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sonidoMision.stop()
                        self.mainMenu()
                        notReady=False


            #Se define el texto, no encontre forma de poner texto con pygame, se tiene que hacer una funcion para gestionar las lineas
            self.screen.fill((0,0,0))
            mission = pygame.font.Font("resources/mission.ttf", 15)
            missionLine1 = mission.render("Greetings commander!",False,(255,255,255))
            missionLine2 = mission.render("Planet Earth cannot sustain us anymore, we need you to colonize a planet.",False,(255,255,255))
            missionLine3 = mission.render("We know you will face many dangers in dark space but...",False,(255,255,255))
            missionLine4 = mission.render("On behalf of our species, we ask you to help us!",False,(255,255,255))
            missionLine5 = mission.render("Or humanity will perish...",False,(255,255,255))
            missionLine6 = mission.render("Farewell commander we hope to see you again...",False,(255,255,255))
            self.screen.blit(missionLine1, (10,40))
            self.screen.blit(missionLine2, (10,120))
            self.screen.blit(missionLine3, (10,160))
            self.screen.blit(missionLine4, (10,200))
            self.screen.blit(missionLine5, (10,240))
            self.screen.blit(missionLine6, (10,300))

            #Se pone el mensaje de escape 
            colores =[(0,0,0), (255,255,255)]
            tecla_escape = pygame.font.Font("resources/espacio.ttf",25)
            tecla_escape_img = tecla_escape.render("Press <ESCAPE> to go back to Menu", False,colores[ix])
            ciclosRefresco +=1
            if ciclosRefresco == retardoAnimacion:
                if ix == 0:
                    ix = 1
                else:
                    ix = 0
                
                ciclosRefresco = 0
            self.screen.blit(tecla_escape_img, (125,400))
            pygame.display.update()


    def mainMenu(self):
        sonidoMenu = mixer.Sound("resources/mainMenu.mp3")
        sonidoMenu.play(-1)
        mainMenu = True
        x=0
        ix=0
        ciclosRefresco=0
        retardoAnimacion = 20
        while mainMenu:
            self.clock.tick(FPS)

            #Movimiento del manu principal
            rel_x = x % self.bgMainMenu.get_rect().width
            self.screen.blit(self.bgMainMenu, (rel_x - self.bgMainMenu.get_rect().width,0))
            if rel_x <= GAME_DIMENSIONS[0]:
                self.screen.blit(self.bgMainMenu, (rel_x,0))
            x -=1
            #Se define el titulo 
            name = pygame.font.Font("resources/titulo.ttf", 90)
            name_img = name.render("THE QUEST",False,(255,179,102))
            self.screen.blit(name_img,(100,150))
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
            self.screen.blit(tecla_espacio_img, (110,350))

            #Se define el boton para leer la historia: 
            tecla_enter = pygame.font.Font("resources/espacio.ttf",25)
            tecla_enter_img = tecla_espacio.render("Press <ENTER> to read about your mission", False,(255,179,102))
            self.screen.blit(tecla_enter_img, (105,450))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainMenu = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sonidoMenu.stop()
                        self.controlsMenu()
                        mainMenu = False
                        
                    if event.key == pygame.K_RETURN:
                        sonidoMenu.stop()
                        self.mission()
                        mainMenu = False
                        

            pygame.display.update()


    def controlsMenu(self):
        sonidoControls = mixer.Sound("resources/controlsMenu.wav")
        sonidoControls.play(-1)
        sonidoControls.set_volume(0.2)
        notReady = True
        while notReady:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    notReady = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sonidoControls.stop()
                        self.mainLoop()
                        notReady=False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sonidoControls.stop()
                        self.mainMenu()
                        notReady = False

            self.screen.fill((0,0,0))
            controls = pygame.font.Font("resources/mission.ttf", 15)
            controls1= pygame.font.Font("resources/mission.ttf", 20)
            keybinds = controls1.render("CONTROLS", False, (255,255,255))
            arrowUp = controls.render("Use arrow UP to move up and release to stop",False,(255,255,255))
            arrowDown = controls.render("Use arrow DOWN to move down and release to stop",False,(255,255,255))
            colide = controls.render("If you colide you will die commander", False,(255,255,255))
            arrowUp_img = pygame.image.load("resources/images/up-arrow.png")
            arrowDown_img= pygame.image.load("resources/images/down-arrow.png")

            
            tecla_espacio = pygame.font.Font("resources/espacio.ttf",25)
            tecla_espacio_img = tecla_espacio.render("Press <SPACE BAR> in order to continue", False,(255,255,255))
            tecla_escape_img = tecla_espacio.render("Press <ESCAPE> to go back to Menu", False,(255,255,255))

            self.screen.blit(keybinds,(360,50))
            self.screen.blit(arrowUp,(230,100))
            self.screen.blit(arrowUp_img,(370, 140))
            self.screen.blit(arrowDown,(230,230))
            self.screen.blit(arrowDown_img,(370,270))
            self.screen.blit(colide,(260,380))
            self.screen.blit(tecla_espacio_img, (110,450))
            self.screen.blit(tecla_escape_img,(150,500))
            pygame.display.update()


    def mainLoop(self):
        sonidoL1 = mixer.Sound("resources/level1.wav")
        sonidoL1.play(-1)
        sonidoL1.set_volume(0.2)
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
            self.pintaObstaculo()
            #self.pintaPlaneta()
            pygame.display.update()
        


class Ship:
    def __init__(self, y, velocidad, x):
        self.y = y 
        self.vy = 0
        self.velocidad = velocidad
        self.neutro = 0
        self.x = x
        self.disfraz = pygame.image.load("resources/images/battleship.png")

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
        elif self.y >= 536:
            self.y = 536
    

class Planeta: 
    def __init__(self,x,y,vx):
        self.x = x
        self.y = y
        self.vx = vx 
        self.planeta_img = pygame.image.load("resources/images/planeta11.png")
        self.planeta_img2 = pygame.image.load("resources/images/planeta22.png")


class Obstaculo:
    def __init__(self):
        self.asteroid = pygame.image.load("resources/images/asteroid.png")
        self.x = 800
        self.y = random.randint(0,536)
        self.statusRunning = 1

    def obstacleUpdate(self):
        if self.statusRunning == 1:
            self.x -= 3
            if self.x == -64:
                self.x = 800
                self.y = random.randint(0,536)

