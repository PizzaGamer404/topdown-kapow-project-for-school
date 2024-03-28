from character import Character, Kapowllet
from vector import Vector, dot
import pygame
import math

class SidewaysDefense:
    def __init__(self, screen, player):
        self.screen: pygame.Surface = screen
        self.player: Character = player
        self.kplts: list[Kapowllet] = []
        self.timer: float = 0
    
    def update(self, room, x_input, y_input, is_pewing, deltatime: float):
        mouse_pos = Vector(*pygame.mouse.get_pos())
        vec_to_mouse = mouse_pos - self.player.position
        left_vel = Vector(-vec_to_mouse.y, vec_to_mouse.x).normalize() * 200

        self.timer -= deltatime

        while self.timer <= 0:
            # Creates slower and weaker kapowllets that move left and right
            time_passed = -self.timer
            self.timer += 0.2
            left_kp = Kapowllet(self.player.position + left_vel * time_passed, left_vel, room, 10, 2)
            right_kp = Kapowllet(self.player.position - left_vel * time_passed, -left_vel, room, 10, 2)
            self.kplts.append(left_kp)
            self.kplts.append(right_kp)
            print("SPAWNING")

        self.kplts = [k for k in self.kplts if k.age < 1]

        for k in self.kplts:
            k.update_kapowllet(deltatime)
    
    def draw(self):
        for k in self.kplts:
            k.draw(self.screen)

class PeriodicExplode:
    class Exploder:
        def __init__(self, screen, position, room):
            self.position: Vector = position
            self.room = room
            self.screen: pygame.Surface = screen

            self.timer: float = 1
            self.hitEnemies: set = set()
        
        def update(self, deltatime: float):
            self.timer -= deltatime
            if self.timer <= -0.25:
                return True
            elif self.timer <= 0:
                explode_size = -self.timer * 300
                # Find enemies within the radius and damage them (record them to avoid damaging 2x)
                for enemy in self.room.enemies:
                    if (enemy.position - self.position).magnitude < explode_size + enemy.radius and enemy not in self.hitEnemies:
                        self.hitEnemies.add(enemy)
                        enemy.health -= 75
            return False
        
        def draw(self):
            # Draws a dot as the exploder or a ring as it explodes
            if self.timer > 0:
                pygame.draw.circle(self.screen, (255, 100, 100), self.position.to_tuple(), 2, 2)
            else:
                explode_size = -self.timer * 300
                pygame.draw.circle(self.screen, (64, 32, 0), self.position.to_tuple(), int(explode_size))
                pygame.draw.circle(self.screen, (255, 0, 0), self.position.to_tuple(), int(explode_size), 5)
        
        

    def __init__(self, screen, player):
        self.screen: pygame.Surface = screen
        self.player: Character = player
        self.kplts: list[Kapowllet] = []
        self.timer: float = 0
        self.exploders: list[PeriodicExplode.Exploder] = []
    
    def update(self, room, x_input, y_input, is_pewing, deltatime: float):
        self.timer -= deltatime

        # Spawn exploders every 0.8 seconds
        while self.timer <= 0:
            self.timer += 0.8
            exp = PeriodicExplode.Exploder(self.screen, self.player.position, room)
            self.exploders.append(exp)

        self.exploders = [e for e in self.exploders if not e.update(deltatime)]
    
    def draw(self):
        for e in self.exploders:
            e.draw()

class AimAssist:
    def __init__(self, screen, player):
        self.screen: pygame.Surface = screen
        self.player: Character = player
    
    def update(self, room, x_input, y_input, is_pewing, deltatime: float):
        for kplt in self.player.kapowllets:
            # Finds the closest enemy to the direction of the kapowllet with dot product
            closest_enemy = None
            closest_dot = -1
            for enemy in room.enemies:
                vec_to_enemy = enemy.position - kplt.position
                vec_to_enemy = vec_to_enemy.normalize()
                d = dot(vec_to_enemy, kplt.velocity.normalize())
                if d > closest_dot:
                    closest_dot = d
                    closest_enemy = enemy
            # If it finds an enemy, moves the velocity towns a new velocity pointing to the enemy
            # Normalizes after this to keep speed
            # Nothing super fancy, I adjusted values to what I thought looked good
            if closest_enemy is not None:
                mag = kplt.velocity.magnitude
                kplt.velocity = kplt.velocity.move_towards(vec_to_enemy.normalize()*mag, mag * deltatime * 3).normalize()*mag
    
    def draw(self):
        pass