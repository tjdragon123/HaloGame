import pygame
import time
import math
from sprite import Sprite
from CentSprite import CentSprite
from Menu import Menu
from Button import Button
from Crosshairs import Crosshairs

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

pygame.init()

pygame.display.init()

pygame.mixer.init() #starts the sound stuff
BMG_50_fires = pygame.mixer.Sound("M 82 Barrett 50 Cal.wav")
#soundtrack = pygame.mixer.music("Halo Theme Song Original.mp3")
pygame.mixer.music.load("Halo Theme Song Original.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("Halo 2D")

"""
crosshairs = CentSprite("haloCrosshairs.png", 0, 0)
crosshairs.change_size(100,80)
crosshairs.recenter()
#orientation = 0
"""
crosshairs = Crosshairs()



level = Sprite("HaloMap.jpg", -500, -500)
level.change_size(400,400)

#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


testPlayer = CentSprite("Blue_Arrow_Up_Darker.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
testPlayer.change_size(10,10)
testPlayer.recenter()

mainMenu = Menu("CEMainMenuBackground.jpg", [Button("playButton.png", 500, 500)])



SPEED = 0.2

print(pygame.time.get_ticks())
lastLoopTime = pygame.time.get_ticks()

inMainMenu = True
gameOver = False
while(not gameOver):
    #orientation += 15
    
    
    while(inMainMenu):
        mainMenu.draw(screen)
        crosshairs.run(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xytuple = pygame.mouse.get_pos()
                if(mainMenu.checkWhichInside(xytuple[0], xytuple[1]) == 0):
                    inMainMenu = False
    
    
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
    
    testPlayer.setDirection(180-math.degrees(math.atan2(crosshairs.crosshairs.cx-(SCREEN_WIDTH/2), crosshairs.crosshairs.cy-(SCREEN_HEIGHT/2))))
    testPlayer.recenter()
    testPlayer.draw(screen)
    
    #crosshairs.draw(screen)
    #crosshairs.setDirection(orientation)
    
    
    
    pygame.display.flip()
    
    
    
    
    
    #if :
     #   BMG_50_fires.play()
     
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            BMG_50_fires.play()
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            inMainMenu == True

print("GAME OVER")
pygame.quit()