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

    # Draws the room
    def __draw__(self):
        self.screen.fill((0, 0, 0))
        self.player.draw()
        