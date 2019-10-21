import pygame
#import time
import math
from sprite import Sprite
from CentSprite import CentSprite
from Menu import Menu
from Button import Button
from Crosshairs import Crosshairs
from Player import Player
#from Enemy import Enemy
#from Weapon import Weapon

enemies = []

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

pygame.init()

pygame.display.init()


pygame.mixer.init() #starts the sound stuff

pygame.mixer.music.load("Halo Theme Song Original.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("Halo 2D")

crosshairs = Crosshairs()

score = 0

level = Sprite("map.png", -500, -500)
level.change_size(150,150)

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


player = Player()

mainMenu = Menu("CEMainMenuBackground.jpg", [Button("playButton.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -50), Button("quitButton.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)])

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)


SPEED = 0.2

print(pygame.time.get_ticks())
lastLoopTime = pygame.time.get_ticks()

inMainMenu = True
gameOver = False
while(not gameOver):
    #orientation += 15
    
    
    while(inMainMenu and not gameOver):
        mainMenu.draw(screen)
        crosshairs.run(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                xytuple = pygame.mouse.get_pos()
                if(mainMenu.checkWhichInside(xytuple[0], xytuple[1]) == 0):
                    inMainMenu = False
                elif(mainMenu.checkWhichInside(xytuple[0], xytuple[1]) == 1):
                    gameOver = True
    
    
    screen.fill((0,0,0))
    
    
    if(pygame.key.get_pressed()[pygame.K_w]):
        level.y += SPEED*(pygame.time.get_ticks()-lastLoopTime)
    if(pygame.key.get_pressed()[pygame.K_s]):
        level.y -= SPEED*(pygame.time.get_ticks()-lastLoopTime)
    if(pygame.key.get_pressed()[pygame.K_a]):
        level.x += SPEED*(pygame.time.get_ticks()-lastLoopTime)
    if(pygame.key.get_pressed()[pygame.K_d]):
        level.x -= SPEED*(pygame.time.get_ticks()-lastLoopTime)
    lastLoopTime = pygame.time.get_ticks()
    
    
    
    level.draw(screen)
    
    """
    crosshairs.cx = pygame.mouse.get_pos()[0]
    crosshairs.cy = pygame.mouse.get_pos()[1]
    crosshairs.recenter()
    """
    crosshairs.run(screen)
    
    """
    testPlayer.setDirection(180-math.degrees(math.atan2(crosshairs.crosshairs.cx-(SCREEN_WIDTH/2), crosshairs.crosshairs.cy-(SCREEN_HEIGHT/2))))
    testPlayer.recenter()
    testPlayer.draw(screen)
    """
    
    player.draw(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 180-math.degrees(math.atan2(crosshairs.crosshairs.cx-(SCREEN_WIDTH/2), crosshairs.crosshairs.cy-(SCREEN_HEIGHT/2))))
    
    
    textsurface = myfont.render('HEALTH : '+str(player.health), False, (255, 0, 0))
    textsurface2 = myfont.render('SHEILD : '+str(player.shields), False, (0, 130, 255))
    textsurface3 = myfont.render('SCORE : '+str(score), False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    screen.blit(textsurface2,(0,25))
    screen.blit(textsurface3,(0,50))
    #crosshairs.draw(screen)
    #crosshairs.setDirection(orientation)
    
    
    
    pygame.display.flip()
    
    
    
    
    
    #if :
     #   BMG_50_fires.play()
     
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            inMainMenu = True

print("GAME OVER")
pygame.quit()