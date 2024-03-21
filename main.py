# To run file: & "C:/Program Files/Blender Foundation/Blender 3.5/3.5/python/bin/python.exe" [file]
# To install package: & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install [package]
# & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install --upgrade pip
import pygame
import time

from character import Character
from room import Room

# Create a 500x500 pixel screen
screen = pygame.display.set_mode((500, 500))
time.sleep(1)

# Creates the player and room
room = Room(screen)
player = room.player


# TODO: 
# Listen for inputs
# Record WASD Arrow Key
# character.move(up, down)
# Call update loops

FRAMERATE = 60
FRAMETIME = 1/FRAMERATE

while True:
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
    # Todo: Update and draw stuff
    room.update(FRAMETIME, x_input, y_input, pewing)
    room.draw()
    pygame.display.flip()
    time.sleep(FRAMETIME)