import random
from Enemy import Enemy

class Spawner:
    
    @staticmethod
    def spawnEnemies(enemies, iteration, scrW, scrH):
        for i in range(0, 3 + iteration):
            z = random.randint(0,3)
            x = 0
            y = 0
            if z == 0:
                x = -100
                y = random.randint(0, scrH)
            if z == 1:
                x = scrW + 100
                y = random.randint(0, scrH)
            if z == 2:
                x = random.randint(0, scrW)
                y = -100
            if z == 3:
                x = random.randint(0, scrW)
                y = scrW + 100
            
            
            enemies.append(Enemy("Sword Elite", 200, "Sprites/MeleeElite.png", 50, x, y, 1, 100))