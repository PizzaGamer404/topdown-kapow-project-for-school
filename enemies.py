import pygame
import random
from vector import Vector

class NormalEnemy:
    def __init__(self, player, spawnposition: Vector):
        self.player = player
        self.health = 100
        self.position = spawnposition
    
    def update(self,deltatime):
        dir_to_player = (self.player.position - self.position).normalize()
        self.position += dir_to_player * 200 * deltatime
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 175, 0), (self.position - Vector(6, 6)).to_tuple, 6)