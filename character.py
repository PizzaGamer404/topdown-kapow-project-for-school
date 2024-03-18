# C:\Users\Student\AppData\Roaming\Python\Python310\Scripts
import pygame

# Class to handle the logic and behaviour of the player
class Character:
    # Makes it easier to access the x and y position of the character
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

    # Creates the player
    def __init__(self, screen: pygame.Surface):
        self.health = 3
        self.position = [screen.get_width()/2,screen.get_height() / 2]
        # Creates a cooldown between when they can "kapow"
        self.kapow_cooldown = 0.0

    # Handles the logic and moves at 400 pixels per second
    # TODO: Prevent moving faster diagonally
    def update(self, x_input: float, y_input: float, deltatime: float, is_pewing: bool):
        # move based on x and y input
        self.x += x_input * deltatime * 400
        self.y += y_input * deltatime * 400
        # The way this is reduced allows it to fall below 0 for 1 frame
        # This is because if the framerate doesn't line up with the cooldown, it might be slowed down
        # This makes it so as they are continually pressing the button, the missed time will accumulate until it kapows a frame earlier
        # If they stop pressing it, then it resets to normal
        if self.kapow_cooldown > 0:
            self.kapow_cooldown -= deltatime
        else:
            self.kapow_cooldown = 0
        # If they are "pewing" and the "kapow" is off cooldown, then "kapow"
        # Todo: we will need to know which direction to do this in, and does it go to the mouse, or in the movement direction?
        if is_pewing and self.kapow_cooldown <= 0.0:
            self.kapow()
            self.kapow_cooldown += 0.25
    
    # Draws the player on the screen (WHITE CIRCLE PLACEHOLDER, REPLACE WITH REAL IMAGE LATER)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x - 10, self.y - 10), 10)

    # Todo: Implement. Needs to be passed to the room so it can be updated, or it can be updated in the character class
    def kapow(self):
        bullet = Kapowllet(self.position, [1, 0])
        raise NotImplementedError("Kapow not implemented yet")

# Class to handle the logic and behaviour of the "kapowllets"
class Kapowllet:
    def __init__(self, position, velocity):
        self.postion = position
        self.velocity = velocity