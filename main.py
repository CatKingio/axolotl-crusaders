import pygame
import sys
import json

class Skill:
    def __init__(self, name, img_path):
        self.name = name
        self.img = pygame.image.load(img_path).convert_alpha()
class Character:
    next_x = 50
    next_y = 250

    def __init__(self, name, role, img, health, attack, defense, speed, skills, is_enemy=False):
        self.img = img
        self.position = (Character.next_x, Character.next_y)
        if is_enemy:
            self.img = pygame.transform.flip(self.img, True, False)
            # Đảo ngược thứ tự chuỗi các kỹ năng nếu là enemy
            skills.reverse()
        Character.next_x += 100
        Character.next_y += 0
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.skills = skills


    def draw(self, screen):
        screen.blit(self.img, self.position)
        # Vẽ các kỹ năng của nhân vật
        x, y = self.position[0], self.position[1] + self.img.get_height() + 10
        for skill in self.skills:
            screen.blit(skill.img, (x, y))
            x += skill.img.get_width() + 10

class CharacterFactory:
    @staticmethod
    def create_character(name, role, img, health, attack, defense, speed, skill_names):
        skills = []
        for skill_name in skill_names:
            img_path = f"img/character_img/{role}/{skill_name}.png"
            skills.append(Skill(skill_name, img_path))
        return Character(name, role, img, health, attack, defense, speed, skills)

def load_characters_from_json(file_path, character_ids):
    with open(f"json/{file_path}.json", 'r') as file:
        data = json.load(file)
    
    characters = []
    for character_id in character_ids:
        if character_id in data:
            character_data = data[character_id]
            for form in character_data["form"]:
                img_path = f"img/character/{form['name']}.png"
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(img, (180, 170))

                skills = []
                for skill in form["skill"]:
                    skills.append(skill[0])

                character = CharacterFactory.create_character(
                    form["name"],
                    character_data["faction"],
                    img,
                    form["hp"][0],  # Chỉ lấy thông tin về mức HP ở cấp độ đầu tiên
                    form["atkPower"][0],  # Tương tự, chỉ lấy thông tin về sức mạnh tấn công ở cấp độ đầu tiên
                    form["armor"][0],  # Và giá trị giáp ở cấp độ đầu tiên
                    form["speed"][0],  # Tốc độ của nhân vật
                    skills
                )
                characters.append(character)

    return characters

# Chọn tối đa 4 nhân vật cho cả hai đội bằng cách liệt kê các ID
ally_character_ids = ["Randgrid", "Leon","Randgrid","Randgrid"]
enemy_character_ids = ["some_enemy_id", "another_enemy_id", "yet_another_enemy_id", "one_more_enemy_id"]

ally_characters = load_characters_from_json("characters_json", ally_character_ids)
enemy_characters = load_characters_from_json("characters_json", ally_character_ids)


# Chọn tối đa 4 nhân vật cho cả hai đội bằng cách liệt kê các ID
ally_character_ids = ["leon", "some_other_character_id", "another_character_id", "yet_another_character_id"]
enemy_character_ids = ["some_enemy_id", "another_enemy_id", "yet_another_enemy_id", "one_more_enemy_id"]

ally_characters = load_characters_from_json("ally_characters.json", ally_character_ids)
enemy_characters = load_characters_from_json("enemy_characters.json", enemy_character_ids)



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

ally_characters = load_characters_from_json("ally_characters.json")
enemy_characters = load_characters_from_json("enemy_characters.json")

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