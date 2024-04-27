# class person:
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         self.name = name
#         self.age = age
#         self.health = health
#         self.shield = shield
#         self.mana = mana
#         self.speed = speed
#         self.skill = skill
    
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Shield: {self.shield}, Mana: {self.mana}, Speed: {self.speed}, Skill: {self.skill}")

# class tanker(person):
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         super().__init__(name, age, health, shield, mana, speed, skill)
        
    
# class warriors(person):
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         super().__init__(name, age, health, shield, mana, speed, skill)
    
# class wizards(person):
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         super().__init__(name, age, health, shield, mana, speed, skill)
        
# class ADC(person):
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         super().__init__(name, age, health, shield, mana, speed, skill)

# class healer(person):
#     def __init__(self, name, age, health, shield, mana, speed, skill):
#         super().__init__(name, age, health, shield, mana, speed, skill)
    
# class event():
#     pass
    
# skillTank_01 = [("Quạt(khiên)", 13), ("Đấm", 23), ("Đá", 33), ("Đỡ", 0)]
# tanker_01 = tanker("Thống", 18, 500, 60, 0, 20, skillTank_01)
# # tanker01.info()

# skillWarriors_01 = [("Chém", 33), ("Đâm", 43), ("Demacia", 53), ("Cắm kiếm", 66)]
# warriors_01 = warriors("Trí", 18, 300, 40, 100, 95, skillWarriors_01)
# # warriors01.info()

# skillWizards_01 = [("FireBall", 85), ("Freeze", 43), ("Boots", 0), ("I am Atomic", 100)]
# wizards_01 = wizards("Quân", 18, 100, 10, 140, 10, skillWizards_01)
# # wizards01.info()

# skillADC_01 = [("Bắn Gọn Gàng", 66), ("Xuyên Táo", 77), ("Đặt Bẫy", 88), ("Bắn Tùm Lum", 99)]
# ADC_01 = ADC("Be Lam", 18, 100, 20, 140, 10, skillWarriors_01)
# # ADC01.info()

# skillHealer_01 = [("Đánh Thường", 10), ("Boots Crit", 0), ("Boots Speed", 0), ("Health", 0)]
# healer_01 = healer("Diễm", 18, 100, 30, 110, 60, skillHealer_01)
# # healer01.info()

# skillTank_02 = [("Quạt(khiên)", 13), ("Đấm", 23), ("Đá", 33), ("Đỡ", 0)]
# tanker_02 = tanker("Th_02", 18, 500, 60, 0, 20, skillTank_02)
# # tanker01.info()

# skillWarriors_02 = [("Chém", 33), ("Đâm", 43), ("Demacia", 53), ("Cắm kiếm", 66)]
# warriors_02 = warriors("Tr_02", 18, 300, 40, 100, 95, skillWarriors_02)
# # warriors01.info()

# skillWizards_02 = [("FireBall", 85), ("Freeze", 43), ("Boots", 0), ("I am Atomic", 100)]
# wizards_02 = wizards("Q_02", 18, 100, 10, 140, 10, skillWizards_02)
# # wizards01.info()

# skillADC_02 = [("Bắn Gọn Gàng", 66), ("Xuyên Táo", 77), ("Đặt Bẫy", 88), ("Bắn Tùm Lum", 99)]
# ADC_02 = ADC("BL_02", 18, 100, 20, 140, 10, skillWarriors_02)
# # ADC01.info()

# skillHealer_02 = [("Đánh Thường", 10), ("Boots Crit", 0), ("Boots Speed", 0), ("Health", 0)]
# healer_02 = healer("Di_02", 18, 100, 30, 110, 60, skillHealer_02)
# # healer01.info()
import pygame

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