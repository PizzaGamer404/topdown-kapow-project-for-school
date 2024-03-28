# To run file: & "C:/Program Files/Blender Foundation/Blender 3.5/3.5/python/bin/python.exe" main.py
# To install package: & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install [package]
# & "C:\Program Files\Blender Foundation\Blender 3.5\3.5\python\bin\python.exe" -m pip install --upgrade pip
import pygame
import time
import random

from character import Character
from room import LevelRoom

pygame.init()

# Create a 500x500 pixel screen
screen = pygame.display.set_mode((750, 750))
time.sleep(1)

PLAYER = Character(screen)
FRAMERATE = 60
FRAMETIME = 1/FRAMERATE

# Force upgrade player for test
from upgrades import SidewaysDefense, PeriodicExplode, AimAssist

upgrade_pool = [SidewaysDefense(screen, PLAYER), PeriodicExplode(screen, PLAYER), AimAssist(screen, PLAYER)]
font = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

def upgrade_selector():
    # shuffle pool
    random.shuffle(upgrade_pool)
    # Skip if no upgrades
    if len(upgrade_pool) == 0:
        return
    # Wait for choice
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Draw text offering the upgrades
        screen.fill((0, 0, 0))
        title = font.render("Choose an upgrade (press number key):", True, (255, 255, 255))
        c1 = font.render("1: " + upgrade_pool[0].__class__.__name__, True, (255, 255, 255)) if len(upgrade_pool) >= 1 else font.render("1: None", True, (255, 255, 255))
        c2 = font.render("2: " + upgrade_pool[1].__class__.__name__, True, (255, 255, 255)) if len(upgrade_pool) >= 2 else font.render("2: None", True, (255, 255, 255))
        c3 = font.render("3: " + upgrade_pool[2].__class__.__name__, True, (255, 255, 255)) if len(upgrade_pool) >= 3 else font.render("3: None", True, (255, 255, 255))
        screen.blit(title, (10, 10))
        screen.blit(c1, (10, 50))
        screen.blit(c2, (10, 90))
        screen.blit(c3, (10, 130))
        pygame.display.flip()
        # Look for key presses and apply the upgrade
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and len(upgrade_pool) >= 1:
            PLAYER.upgrades.append(upgrade_pool[0])
            del upgrade_pool[0]
            return
        elif keys[pygame.K_2] and len(upgrade_pool) >= 2:
            PLAYER.upgrades.append(upgrade_pool[1])
            del upgrade_pool[1]
            return
        elif keys[pygame.K_3] and len(upgrade_pool) >= 3:
            PLAYER.upgrades.append(upgrade_pool[2])
            del upgrade_pool[2]
            return
room_count = 0

def update_level_room(room: LevelRoom):
    if PLAYER.health <= 0:
        pygame.quit()
    time.sleep(FRAMETIME)
    # Listen for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Record WASD Arrow Key
    keys = pygame.key.get_pressed()
    # Reads WASD inputs
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
    # Reads m1 or spacebar for pewing
    pewing = pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]
    # Call update and draw functions
    room.update(FRAMETIME, x_input, y_input, pewing)
    room.draw()
    # Draw room counter
    room_counter = font_small.render("Room: " + str(room_count), True, (255, 255, 255))
    screen.blit(room_counter, (10, 10))
    # Finally update the screen
    pygame.display.flip()


while True:
    room_count += 1
    room: LevelRoom = LevelRoom(screen, PLAYER, room_count+2, room_count+1, room_count//2-1)
    time_empty = 0
    while True:
        # End the loop after 2 second with no enemoes
        if len(room.enemies) == 0:
            time_empty += FRAMETIME
            if time_empty > 1:
                break
        update_level_room(room)
    if room_count % 3 == 0:
        upgrade_selector()