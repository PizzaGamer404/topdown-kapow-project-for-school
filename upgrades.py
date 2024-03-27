from character import Character, Kapowllet
from vector import Vector
import pygame

class SidewaysDefense:
    def __init__(self, screen, player):
        self.screen: pygame.Surface = screen
        self.player: Character = player
        self.kplts: list[Kapowllet] = []
        self.timer: float = 0
    
    def update(self, room, x_input, y_input, is_pewing, deltatime: float):
        mouse_pos = Vector(*pygame.mouse.get_pos())
        vec_to_mouse = mouse_pos - self.player.position
        left_vel = Vector(-vec_to_mouse.y, vec_to_mouse.x).normalize() * 120

        self.timer -= deltatime

        while self.timer <= 0:
            time_passed = -self.timer
            self.timer += 0.25
            # left_kp = Kapowllet(self.player.position + left_vel * time_passed, left_vel, room, 7, 2)
            # right_kp = Kapowllet(self.player.position - left_vel * time_passed, -left_vel, room, 7, 2)
            left_kp = Kapowllet(self.player.position * time_passed, left_vel, room, 7, 2)
            right_kp = Kapowllet(self.player.position * time_passed, -left_vel, room, 7, 2)
            self.kplts.append(left_kp)
            self.kplts.append(right_kp)
            print("SPAWNING")

        self.kplts = [k for k in self.kplts if k.age < 1]

        for k in self.kplts:
            k.update_kapowllet(deltatime)
    
    def draw(self):
        for k in self.kplts:
            k.draw(self.screen)