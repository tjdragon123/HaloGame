import pygame
#import time
import math
from sprite import Sprite
from CentSprite import CentSprite
from Menu import Menu
from Button import Button
from Crosshairs import Crosshairs
from Player import Player
from Enemy import Enemy
#from Weapon import Weapon
from Spawner import Spawner

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


level = Sprite("map.png", -500, -500)
level.change_size(150,150)

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


player = Player()

mainMenu = Menu("CEMainMenuBackground.jpg", [Button("playButton.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -50), Button("quitButton.png", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)])

#STAT BOARD
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
score = 0
board = Sprite("Sprites\\Bar.png",-5,-5)
board.change_size(28,17)

SPEED = 0.2


lastLoopTime = pygame.time.get_ticks()
lastEnemyTime = lastLoopTime

spawnFreq = 10000
lastSpawn = -100000
iteration = 1

postGame = True
inMainMenu = True
gameOver = False


while(not gameOver):

    
    
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
    
    lastLoopTime = pygame.time.get_ticks()
    
    while(not inMainMenu and not gameOver):
        
        screen.fill((0,0,0))
        
        
        
        WASD = [pygame.key.get_pressed()[pygame.K_w], pygame.key.get_pressed()[pygame.K_a], pygame.key.get_pressed()[pygame.K_s], pygame.key.get_pressed()[pygame.K_d]]
        
        amtx = 0
        amty = 0
        
        if WASD[0] and WASD[1] and WASD[2] and WASD[3]:
            pass
        
        elif WASD[0] and not WASD[2]:
            if WASD[1] and not WASD[3]:
                amtx = -0.70710678118
                amty = -0.70710678118
            elif WASD[3] and not WASD[1]:
                amtx = 0.70710678118
                amty = -0.70710678118
            else:
                amty = -1
        
        elif WASD[2] and not WASD[0]:
            if WASD[1] and not WASD[3]:
                amtx = -0.70710678118
                amty = 0.70710678118
            elif WASD[3] and not WASD[1]:
                amtx = 0.70710678118
                amty = 0.70710678118
            else:
                amty = 1
        
        elif WASD[1] and not WASD[3]:
            amtx = -1
        
        elif WASD[3] and not WASD[1]:
            amtx = 1
        
        amtx *= -1
        amty *= -1
        
        currentTime = pygame.time.get_ticks()
        
        level.x += amtx*SPEED*(currentTime-lastLoopTime)
        level.y += amty*SPEED*(currentTime-lastLoopTime)
        for enemy in enemies:
            enemy.sprite.cx += amtx*SPEED*(currentTime-lastLoopTime)
            enemy.sprite.cy += amty*SPEED*(currentTime-lastLoopTime)
            enemy.sprite.recenter()
        
        lastLoopTime = pygame.time.get_ticks()
        
        
        
        level.draw(screen)
        
        
        if (currentTime - lastSpawn) >= spawnFreq:
            Spawner.spawnEnemies(enemies, iteration, SCREEN_WIDTH, SCREEN_HEIGHT)
            iteration += 1
            lastSpawn = currentTime
        
        for enemy in enemies:
            if enemy.health <= 0:
                score += enemy.points
                enemies.remove(enemy)
            else:
                enemy.doBehavior(player, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, lastEnemyTime, pygame.time.get_ticks())
                enemy.sprite.draw(screen)
        
        lastEnemyTime = pygame.time.get_ticks()
        
        if player.health <= 0:
            gameOver = True
        
        crosshairs.run(screen)
        
        
        direction = 90+math.degrees(math.atan2(crosshairs.crosshairs.cy-(SCREEN_HEIGHT/2), crosshairs.crosshairs.cx-(SCREEN_WIDTH/2)))
        print("direction: " + str(direction))
        player.draw(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, direction)
        player.current.firing = False
        
        textsurface = myfont.render('HEALTH : '+str(player.health), False, (255, 0, 0))
        textsurface2 = myfont.render('SHIELD : '+str(player.shields), False, (0, 130, 255))
        textsurface3 = myfont.render('SCORE : '+str(score), False, (255, 255, 255))
        board.draw(screen)
        screen.blit(textsurface,(0,0))
        screen.blit(textsurface2,(0,25))
        screen.blit(textsurface3,(0,50))
        
        crosshairs.run(screen)
        
        pygame.display.flip()
        
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot(enemies, direction, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, pygame.time.get_ticks())
            if event.type == pygame.QUIT:
                gameOver = True
                postGame = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                inMainMenu = True
        

gameoverFont = pygame.font.SysFont('Comic Sans MS', 100)
gameoverSurface = gameoverFont.render('GAME OVER', False, (255, 0, 0))
scoreFont = pygame.font.SysFont('Comic Sans MS', 50)
scoreSurface = scoreFont.render('SCORE: ' + str(score), False, (255, 0, 0))

while(postGame):
    screen.fill((0,0,0))
    screen.blit(gameoverSurface,(0,0))
    screen.blit(scoreSurface,(0,200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            postGame = False

print("GAME OVER")
pygame.quit()