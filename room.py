# C:\Users\Student\AppData\Roaming\Python\Python310\Scripts
import pygame
from character import Character

class Room:
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

    # Initializez the room
    def __init__(self, screen: pygame.Surface, player: Character):
        self.screen = screen
        self.player: Character = player
    
    def update(self, deltatime, x_input, y_input, pewing):
        self.player.update(x_input,y_input,deltatime, pewing)

    # Draws the room and player
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        