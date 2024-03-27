# C:\Users\Student\AppData\Roaming\Python\Python310\Scripts
import pygame
from vector import Vector
from enemies import NormalEnemy
from character import Character
import random

class LevelRoom:
    # Width of the screen
    @property
    def width(self) -> int:
        return self.screen.get_width()

    # Height of the screen
    @property
    def height(self) -> int:
        return self.screen.get_height()

    # Center of the screen
    @property
    def center(self) -> tuple[int, int]:
        return self.screen.get_width() // 2, self.screen.get_height() // 2

    # Initializes the room
    def __init__(self, screen: pygame.Surface, player: Character):
        self.screen = screen
        self.player: Character = player
        self.enemies = [NormalEnemy(self.player, Vector(random.uniform(0, self.width), random.uniform(0, self.height)), screen) for _ in range(15)]

    
    def update(self, deltatime, x_input, y_input, pewing):
        self.player.update(x_input,y_input,deltatime, pewing, self)
        for enemy in self.enemies:
            enemy.update(deltatime)

    # Draws the room and player
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw()