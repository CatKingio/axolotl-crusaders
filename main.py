import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Axolotl Crusaders")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


running = True
ally_turn = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass
         

# Kết thúc Pygame
pygame.quit()
sys.exit()
