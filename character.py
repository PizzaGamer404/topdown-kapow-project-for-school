# C:\Users\Student\AppData\Roaming\Python\Python310\Scripts
import pygame
from vector import Vector

smile = pygame.image.load('smil.png')
smile_size = Vector(smile.get_width(), smile.get_height())

# Class to handle the logic and behaviour of the player
class Character:
    # Creates the player
    def __init__(self, screen: pygame.Surface):
        self.health = 3
        self.position: Vector = Vector(screen.get_width()/2, screen.get_height() / 2)
        # Creates a cooldown between when they can "kapow"
        self.kapow_cooldown = 0.0
        # Holds kapowllets
        self.kapowllets: list[Kapowllet] = []
        self.normal_color = (80, 199, 199)
        self.invincible_color_1 = (60, 149, 149)
        self.invincible_color_2 = (80//2, 199//2, 199//2)
        self.damage_invincibility: float = 0
        self.upgrades = []
    # Handles the logic and moves at 400 pixels per second
    def update(self, x_input: float, y_input: float, deltatime: float, is_pewing: bool, room):
        self.damage_invincibility -= deltatime
        mouse_pos = Vector(*pygame.mouse.get_pos())
        dir_to_mouse = (mouse_pos - self.position).normalize()
        # Normalize inputs if they are greater than 1
        input = Vector(x_input, y_input)
        if input.magnitude > 1:
            input = input.normalize()
        # move based on x and y input
        self.position += input * 300 * deltatime
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
            self.kapow(dir_to_mouse, room)
            self.kapow_cooldown += 0.25
        # Todo: Despawn old kapowllets
        # Update kapowllets
        for kapowllet in self.kapowllets:
            kapowllet.update_kapowllet(deltatime)

        # Clamp to be within the screen. room.width, room.height show the size of the screen
        if self.position.x > room.width - 10:
            self.position.x = room.width - 10
        elif self.position.x < 10:
            self.position.x = 10
        if self.position.y > room.height - 10:
            self.position.y = room.height - 10
        elif self.position.y < 10:
            self.position.y = 10
        

        # Run upgrades
        for u in self.upgrades:
            u.update(room, x_input, y_input, is_pewing, deltatime)
    # Draws the player on the screen (WHITE CIRCLE PLACEHOLDER, REPLACE WITH REAL IMAGE LATER)
    def draw(self, screen: pygame.Surface):
        if self.damage_invincibility <= 0:
            pygame.draw.circle(screen, (80, 199, 199), (self.position.x, self.position.y), 10)
        # Alternates invincibility color
        elif self.damage_invincibility % 1 < 0.5:
            pygame.draw.circle(screen, self.invincible_color_1, (self.position.x, self.position.y), 10)
        else:
            pygame.draw.circle(screen, self.invincible_color_2, (self.position.x, self.position.y), 10)
        # Draw kapowllets
        for kapowllet in self.kapowllets:
            kapowllet.draw(screen)
        # Draw health
        for i in range(self.health):
            pygame.draw.circle(screen, (125, 125, 125), (50 + i*25, screen.get_height()-50), 9)
            screen.blit(smile, (50 + i*25 - smile_size[0]//2, screen.get_height() - 50 - smile_size[1]//2))
        
        for u in self.upgrades:
            u.draw()

    # Todo: Implement. Needs to be passed to the room so it can be updated, or it can be updated in the character class
    def kapow(self, direction, room, damage=25):
        # FIlter kapowllets that are too old
        self.kapowllets = [kapowllet for kapowllet in self.kapowllets if kapowllet.age < 2]
        # Create a bullet traveling 800 pixels per second
        kapowlette = Kapowllet(self.position, direction * 800, room, damage)
        # Records itlli
        self.kapowllets.append(kapowlette)
    
    def take_damage(self):
        if self.damage_invincibility > 0:
            return
        self.health -= 1
        self.damage_invincibility = 3

# Class to handle the logic and behaviour of the "kapowllets"
class Kapowllet:
    def __init__(self, position, velocity, room, damage=25, radius=3):
        self.position: Vector = position
        self.velocity: Vector = velocity
        self.room = room
        self.age: float = 0
        self.damage = damage
        self.radius = radius
        
    def update_kapowllet(self, delatime):
        self.position += (self.velocity * delatime)
        self.age += delatime

        for enemy in self.room.enemies:
            if (enemy.position - self.position).magnitude < (self.radius + enemy.radius):
                enemy.health -= self.damage


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius)
