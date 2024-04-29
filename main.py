import pygame
import sys
import json
import os

# Load character data from JSON file
with open("json/characters_json.json", 'r') as file:
    data = json.load(file)

# Initialize pygame
pygame.init()

# Define Skill class
class Skill:
    def __init__(self, name, img_path):
        self.name = name
        self.img = pygame.image.load(img_path).convert_alpha()
  

class Battle:
    def __init__(self, screen, ally_character_ids, enemy_character_ids):
        self.screen = screen
        self.ally_characters = load_and_create_characters_from_json(ally_character_ids)
        self.enemy_characters = load_and_create_characters_from_json(enemy_character_ids, True)
        self.setup_characters_positions()
        self.current_frame = 0
        self.update_time = pygame.time.get_ticks()

    def setup_characters_positions(self):
        total_slots = 9  # Total number of slots on the battlefield
        ally_slots_allowed = 4  # Number of slots allowed for ally team
        enemy_slots_allowed = 4  # Number of slots allowed for enemy team
        slot_width = screen_width / total_slots  # Calculate the width of each slot
        character_scale = 0.9
        ally_slot_count = 0
        for character in self.ally_characters:
            slot = min(character.slot, ally_slots_allowed - ally_slot_count)
            character_width = slot_width * slot * character_scale
            character_height = character.animation_images[0].get_height() / character.animation_images[0].get_width() * character_width
            x = slot_width * (ally_slot_count + slot / 2) - character_width / 2 + 10
            y = screen_height * 0.45 - character_height / 2
            for i, img in enumerate(character.animation_images):
                character.animation_images[i] = pygame.transform.scale(img, (int(character_width), int(character_height)))
            character.rect = character.animation_images[0].get_rect(topleft=(x, y))
            ally_slot_count += slot

        enemy_slot_count = 0
        for character in self.enemy_characters:
            slot = min(character.slot, enemy_slots_allowed - enemy_slot_count)
            character_width = slot_width * slot * character_scale
            character_height = character.animation_images[0].get_height() / character.animation_images[0].get_width() * character_width
            x = screen_width - slot_width * (enemy_slot_count + slot / 2) - character_width / 2 - 10
            y = screen_height * 0.45 - character_height / 2
            for i, img in enumerate(character.animation_images):
                character.animation_images[i] = pygame.transform.scale(img, (int(character_width), int(character_height)))
            character.rect = character.animation_images[0].get_rect(topleft=(x, y))
            if character.is_enemy:
                for i, img in enumerate(character.animation_images):
                    character.animation_images[i] = pygame.transform.flip(img, True, False)
            enemy_slot_count += slot

  
    
    def draw_animation(self, character, current_frame):
        if hasattr(character, 'animation_images'):
            self.screen.blit(character.animation_images[current_frame], character.rect.topleft)
    
    def update(self):
        animation_time = 100
        if pygame.time.get_ticks() - self.update_time > animation_time:
            self.update_time = pygame.time.get_ticks()
            self.current_frame = (self.current_frame + 1) % len(self.ally_characters[0].animation_images)  # Sử dụng chiều dài của danh sách hình ảnh của một nhân vật bất kỳ
    
    def draw_battlefield(self):
        for character in self.ally_characters + self.enemy_characters:
            self.draw_animation(character, self.current_frame)





# Define Character class
class Character:
    def __init__(self, builder):
        self.name = builder.name
        self.faction = builder.faction
        self.role = builder.role
        self.is_enemy = builder.is_enemy
        self.health = builder.hp
        self.attack = builder.atkPower
        self.defense = builder.armor
        self.speed = builder.speed
        self.star = builder.star
        self.level = builder.level
        self.critChance = builder.critChance
        self.critDamage = builder.critDamage
        self.resistance = builder.resistance
        self.accuracy = builder.accuracy
        self.evasion = builder.evasion
        self.penetrate = builder.penetrate
        self.skill = builder.skill
        self.slot = builder.slot
        self.background = builder.background
        self.how_to_get = builder.how_to_get
        self.img = builder.img
        if self.img is None:
            self.load_img()
    def load_img(self):
        self.animation_images = []  
        animation_folder = f"img/characters_img/{self.role}/{self.name}/stand/"
        for i in range(1, 5):  # Assumed 4 animation images
            img_path = os.path.join(animation_folder, f"{self.name}_{i}.png".lower())
            self.img = pygame.image.load(img_path).convert_alpha()
            self.animation_images.append(self.img)
    def draw_animation(self, screen, current_frame):
        # Vẽ hình ảnh của frame hiện tại
        screen.blit(self.animation_images[current_frame], (self.x, self.y))


# Define CharacterBuilder class
class CharacterBuilder:
    def __init__(self, name):
        self.name = name
        self.faction = ""
        self.role = ""
        self.is_enemy = True
        self.hp = 0
        self.atkPower = 0
        self.armor = 0
        self.speed = 0
        self.star = 0
        self.level = 0
        self.critChance = 0.0
        self.critDamage = 0.0
        self.resistance = 0.0
        self.accuracy = 0.0
        self.evasion = 0.0
        self.penetrate = 0.0
        self.skill = []
        self.slot = 0
        self.background = ""
        self.how_to_get = []
        self.img = None

    def set_faction(self, faction):
        self.faction = faction
        return self

    def set_role(self, role):
        self.role = role
        return self

    def set_enemy(self, is_enemy):
        self.is_enemy = is_enemy
        return self

    def set_hp(self, hp):
        self.hp = hp
        return self

    def set_atkPower(self, atkPower):
        self.atkPower = atkPower
        return self

    def set_armor(self, armor):
        self.armor = armor
        return self

    def set_speed(self, speed):
        self.speed = speed
        return self

    def set_star(self, star):
        self.star = star
        return self

    def set_level(self, level):
        self.level = level
        return self

    def set_critChance(self, critChance):
        self.critChance = critChance
        return self

    def set_critDamage(self, critDamage):
        self.critDamage = critDamage
        return self

    def set_resistance(self, resistance):
        self.resistance = resistance
        return self

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy
        return self

    def set_evasion(self, evasion):
        self.evasion = evasion
        return self

    def set_penetrate(self, penetrate):
        self.penetrate = penetrate
        return self

    def set_skill(self, skill):
        self.skill = skill
        return self

    def set_slot(self, slot):
        self.slot = slot
        return slot
    
    def set_background(self, background):
        self.background = background
        return self

    def set_how_to_get(self, how_to_get):
        self.how_to_get = how_to_get
        return self

    def set_img(self, img):
        self.img = img
        return self

    def build(self):
        return Character(self)

class CharacterFactory:
    @staticmethod
    def create_character(name, is_enemy=True):  # Add is_enemy parameter
        builder = CharacterBuilder(name)
        if name in data:
            character_data = data[name]
            form = character_data["form"][0]  # Take the first form for simplicity
            builder.set_faction(character_data.get("faction", ""))
            builder.set_role(character_data.get("role", ""))
            builder.set_hp(form.get("hp", [0])[0])
            builder.set_atkPower(form.get("atkPower", [0])[0])
            builder.set_armor(form.get("armor", [0.0])[0])
            builder.set_speed(form.get("speed", [0])[0])
            builder.set_star(form.get("star", 0))
            builder.set_level(form.get("level", 0))
            builder.set_critChance(form.get("critChance", 0.0))
            builder.set_critDamage(form.get("critDamage", 0.0))
            builder.set_resistance(form.get("resistance", 0.0))
            builder.set_accuracy(form.get("accuracy", 0.0))
            builder.set_evasion(form.get("evasion", 0.0))
            builder.set_penetrate(form.get("penetrate", 0.0))
            builder.set_skill(form.get("skill", []))
            builder.set_slot(form.get("slot", 0))
            builder.set_background(character_data.get("background", ""))
            builder.set_how_to_get(form.get("howToGet", []))
            builder.set_enemy(is_enemy)  # Set is_enemy attribute based on parameter
        return builder.build()


def load_and_create_characters_from_json(character_ids, is_enemy=False):
    characters = []
    for character_id in character_ids:
        characters.append(CharacterFactory.create_character(character_id))
    return characters



# Define function to draw background image
def draw_img(screen, img, width, height, x, y):
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x, y))

# Set up pygame display
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Axolotl Crusaders")

# Load background and panel images
background_img = pygame.image.load("img/background/bg_1.jpg").convert_alpha()
panel_img = pygame.image.load("img/assets/panel.png").convert_alpha()
def main():
    ally_character_ids = ["Randgrid", "Randgrid", "Randgrid", "Randgrid"]
    enemy_character_ids = ["Randgrid", "Randgrid", "Randgrid", "Randgrid"]

    clock = pygame.time.Clock()
    fps = 60
    running = True

    battle = Battle(screen, ally_character_ids, enemy_character_ids)

    while running:
        clock.tick(fps)
        
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_img(screen, background_img, screen.get_width(), int(screen.get_height() * 0.6), 0, 0)
        draw_img(screen, panel_img, screen.get_width(), int(screen.get_height() * 0.4), 0, int(screen.get_height() * 0.6))
        battle.update()
        battle.draw_battlefield()

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
