import pygame
import time
from sprite import Sprite

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

crosshairs = Sprite("haloCrosshairs.png", 0, 0)
crosshairs.change_size(100,80)

level = Sprite("HaloMap.jpg", -500, -500)
level.change_size(400,400)

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

testPlayer = Sprite("Blue_Arrow_Up_Darker.png", (SCREEN_WIDTH/2)-30, (SCREEN_HEIGHT/2)-30)
testPlayer.change_size(10,10)

SPEED = 3

gameOver = False
while(not gameOver):
    screen.fill((0,0,0))
    
    if(pygame.key.get_pressed()[pygame.K_w]):
        level.y += SPEED
    if(pygame.key.get_pressed()[pygame.K_s]):
        level.y -= SPEED
    if(pygame.key.get_pressed()[pygame.K_a]):
        level.x += SPEED
    if(pygame.key.get_pressed()[pygame.K_d]):
        level.x -= SPEED
    
    
    
    
    level.draw(screen)
    
    testPlayer.draw(screen)
    
    crosshairs.x = pygame.mouse.get_pos()[0]
    crosshairs.y = pygame.mouse.get_pos()[1]
    crosshairs.draw(screen)
    
    
    
    pygame.display.flip()
    
    
    
    
    
    #if :
     #   BMG_50_fires.play()
     
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            BMG_50_fires.play()
        if event.type == pygame.QUIT:
            gameOver = True

print("GAME OVER")
pygame.quit()