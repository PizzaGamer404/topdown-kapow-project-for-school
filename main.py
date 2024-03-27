# To run file: & "C:/Program Files/Blender Foundation/Blender 3.5/3.5/python/bin/python.exe" main.py
# To install package: & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install [package]
# & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install --upgrade pip
import pygame
import time

from character import Character
from room import LevelRoom

# Create a 500x500 pixel screen
screen = pygame.display.set_mode((500, 500))
time.sleep(1)

PLAYER = Character(screen)
FRAMERATE = 60
FRAMETIME = 1/FRAMERATE

def update_level_room(room: LevelRoom):
    if Character.health <= 0:
        pygame.quit()
    time.sleep(FRAMETIME)
    # Listen for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Record WASD Arrow Key
    keys = pygame.key.get_pressed()
    x_input = 0
    y_input = 0
    if keys[pygame.K_w]:
        y_input = -1
    if keys[pygame.K_s]:
        y_input = 1
    if keys[pygame.K_a]:
        x_input = -1
    if keys[pygame.K_d]:
        x_input = 1
    pewing = pygame.mouse.get_pressed()[0]
    room.update(FRAMETIME, x_input, y_input, pewing)
    room.draw()
    pygame.display.flip()

while True:
    room: LevelRoom = LevelRoom(screen, PLAYER)
    time_empty = 0
    while True:
        # End the loop after 2 second with no enemoes
        if len(room.enemies) == 0:
            time_empty += FRAMETIME
            if time_empty > 2:
                break
        update_level_room(room)