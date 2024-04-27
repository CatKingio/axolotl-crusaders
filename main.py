import pygame
import sys
from character import *

class Character:
    next_x = 50
    next_y = 250

    def __init__(self, img_path, is_enemy=False):
        self.img = pygame.image.load(img_path).convert_alpha()
        self.img = pygame.transform.scale(self.img, (180, 170))
        if is_enemy:
            self.img = pygame.transform.flip(self.img, True, False)  # Lật hình ảnh theo chiều ngang
            self.position = (Character.next_x + 200, Character.next_y)  # Thêm 200 vào vị trí x của nhân vật địch
        else:
            self.position = (Character.next_x, Character.next_y)
        Character.next_x += 100  # Tăng x lên mỗi khi tạo một nhân vật mới
        Character.next_y += 0     # Giữ y không đổi

    def draw(self, screen):
        screen.blit(self.img, self.position)

class CharacterFactory:
    @staticmethod
    def create_character(img_path, is_enemy=False):
        return Character(img_path, is_enemy)

def draw_background_img(screen, img, width, height):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (0, 0))

def draw_panel_img(screen, img, width, height, battle_height):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (0, battle_height))
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1200
screen_height = 700
screen_battle_width = screen_width
screen_battle_height = 500
screen_panel_width = screen_width
screen_panel_height = screen_height - screen_battle_height

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Axolotl Crusaders")

background_img = pygame.image.load("img/background/bg_1.jpg").convert_alpha()
panel_img = pygame.image.load("img/assets/panel.png").convert_alpha()

# Tạo đội của bạn
ally_characters = []



ally_characters.append(CharacterFactory.create_character("img/character/healer/character_3.png"))
ally_characters.append(CharacterFactory.create_character("img/character/mage/character_3.png"))
ally_characters.append(CharacterFactory.create_character("img/character/warrior/character_1.png"))
ally_characters.append(CharacterFactory.create_character("img/character/tank/character_4.png"))

# Tạo đội địch
enemy_characters = []

enemy_characters.append(CharacterFactory.create_character("img/character/boss/character_3.png", is_enemy=True))
enemy_characters.append(CharacterFactory.create_character("img/character/boss/character_18.png", is_enemy=True))
enemy_characters.append(CharacterFactory.create_character("img/character/boss/character_16.png", is_enemy=True))
enemy_characters.append(CharacterFactory.create_character("img/character/boss/character_8.png", is_enemy=True))

running = True
ally_turn = True 
while running:
    clock.tick(fps)
    draw_background_img(screen, background_img, screen_battle_width, screen_battle_height)
    draw_panel_img(screen, panel_img, screen_panel_width, screen_panel_height, screen_battle_height)
    
    # Vẽ nhân vật trong đội của bạn
    for character in ally_characters:
        character.draw(screen)

    # Vẽ nhân vật trong đội địch
    for character in enemy_characters:
        character.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass
         
    pygame.display.update()

pygame.quit()
sys.exit()
