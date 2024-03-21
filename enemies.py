import pygame
import random
from vector import Vector, lerp

class NormalEnemy:
    def __init__(self, player, spawnposition: Vector, screen):
        self.player = player
        self.health = 100
        self.position = spawnposition
        self.screen = screen
        self.radius = 8
        self.target_position: Vector = player.position
        self.speed_multiplier: float = 0
    
    def update(self,deltatime):
        self.speed_multiplier = min(self.speed_multiplier + deltatime/2, 1)
        self.position = self.position.move_towards(self.target_position, 250*deltatime*self.speed_multiplier)
        if self.position == self.target_position:
            if random.randrange(10) > 0:
                self.target_position = lerp(self.position, self.player.position, random.uniform(0.5, 1))
            else:
                self.target_position = Vector(random.uniform(0, self.screen.get_width()), random.uniform(0, self.screen.get_height()))
        
        if (self.position - self.player.position).magnitude < self.radius + 10:
            self.player.take_damage()
        
    def draw(self):
        # Draw line from position to taget position
        # pygame.draw.line(self.screen, (255, 255, 255), self.position.to_tuple(), self.target_position.to_tuple(), 2)
        pygame.draw.circle(self.screen, (0, 175, 0), (self.position).to_tuple(), self.radius)
