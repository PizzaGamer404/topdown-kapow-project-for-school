# To run file: & "C:/Program Files/Blender Foundation/Blender 3.5/3.5/python/bin/python.exe" [file]
# To install package: & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install [package]
import pygame
import time

from character import Character
from room import Room

# Create a 500x500 pixel screen
screen = pygame.display.set_mode((500, 500))
time.sleep(1)

# Creates the player and room
player = Character(screen)
room = Room(screen, player)

# TODO: 
# Listen for inputs
# Record WASD Arrow Key
# character.move(up, down)
# Call update loops