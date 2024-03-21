import pygame
import random
from vector import Vector

class NormalEnemy:
    def __init__(self, player, spawnposition: Vector, screen):
        self.player = player
        self.health = 100
        self.position = spawnposition
        self.screen = screen
        self.radius = 8
    
    def update(self,deltatime):
        dir_to_player = (self.player.position - self.position).normalize()
        self.position += dir_to_player * 200 * deltatime
    
    def draw(self):
        pygame.draw.circle(self.screen, (0, 175, 0), (self.position - Vector(self.radius, self.radius)).to_tuple(), self.radius)
