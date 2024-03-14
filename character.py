# C:\Users\Student\AppData\Roaming\Python\Python310\Scripts
import pygame

class Character:
    @property
    def x(self) -> float:
        return self.position[0]
    @property.setter
    def x(self, value: float):
        self.position[0] = value
    @property
    def y(self) -> float:
        return self.position[1]
    @property.setter
    def y(self, value: float):
        self.position[1] = value


    def __init__(self, screen: pygame.Surface):
        self.health = 3
        self.position = [screen.get_width()/2,screen.get_height() / 2]
        self.kapow_cooldown = 0.0
    def move(self, x_input: float, y_input: float):
        if x_input == 1.0:
            self.x += 1.0
        elif x_input == 2.0:
            self.x -= 1.0
        if y_input == 1.0:
            self.y += 1.0
        elif y_input == 2.0:
            self.y -= 1.0
    
    def draw(self, screen):
        raise NotImplementedError

    def update(self, deltatime: float, is_pewing: bool):
        if self.kapow_cooldown > 0:
            self.kapow_cooldown -= deltatime
        else:
            self.kapow_cooldown = 0

        if is_pewing and self.kapow_cooldown <= 0.0:
            self.kapow()
            self.kapaw_cooldown += 0.25

    def kapow(self):
        bullet = Kapowllet(self.position, [1, 0])
    
class Kapowllet:
    def __init__(self, position, velocity):
        self.postion = position
        self.velocity = velocity