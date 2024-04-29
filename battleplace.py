from character import *
from skill import *

class battle:
    def __init__(self, ally, enemy, all_character):
        self.ally = ally
        self.enemy = enemy 
        self.all_character = all_character
        
    def info_battle(self):
        list_turn = []
        for self.character in self.all_character:
            list_turn.append([self.character[0].name, self.character[1]])
            
        print(self.ally)
        
        print(list_turn)
        
        print(self.all_character)
        self.health_my_team = self.ally[0].health + self.ally[1].health + self.ally[2].health + self.ally[3].health
        self.health_enemy_team = self.enemy[0].health + self.enemy[1].health + self.enemy[2].health + self.enemy[3].health
        
        self.index_character = 0
        
        while (self.health_my_team > 0)  or (self.health_enemy_team > 0):
            
            print("My_Team")
            print(f"{self.ally[0].name}\t\t|\t\t{self.ally[1].name}\t\t|\t\t{self.ally[2].name}\t\t|\t\t{self.ally[3].name}")
            print(f"{self.ally[0].health}\t\t|\t\t{self.ally[1].health}\t\t|\t\t{self.ally[2].health}\t\t|\t\t{self.ally[3].health}")
            print(f"{self.ally[0].mana}\t\t|\t\t{self.ally[1].mana}\t\t|\t\t{self.ally[2].mana}\t\t|\t\t{self.ally[3].mana}")
            print(f"{self.ally[0].speed}\t\t|\t\t{self.ally[1].speed}\t\t|\t\t{self.ally[2].speed}\t\t|\t\t{self.ally[3].speed}")
            print(f"{self.ally[0].skill}\t\t|\t\t{self.ally[1].skill}\t\t|\t\t{self.ally[2].skill}\t\t|\t\t{self.ally[3].skill}")
            
            print("Enemy_Team") 
            print(f"{self.enemy[0].name}\t\t|\t\t{self.enemy[1].name}\t\t|\t\t{self.enemy[2].name}\t\t|\t\t{self.enemy[3].name}")
            print(f"{self.enemy[0].health}\t\t|\t\t{self.enemy[1].health}\t\t|\t\t{self.enemy[2].health}\t\t|\t\t{self.enemy[3].health}")
            print(f"{self.enemy[0].mana}\t\t|\t\t{self.enemy[1].mana}\t\t|\t\t{self.enemy[2].mana}\t\t|\t\t{self.enemy[3].mana}")
            print(f"{self.enemy[0].speed}\t\t|\t\t{self.enemy[1].speed}\t\t|\t\t{self.enemy[2].speed}\t\t|\t\t{self.enemy[3].speed}")
            print(f"{self.enemy[0].skill}\t\t|\t\t{self.enemy[1].skill}\t\t|\t\t{self.enemy[2].skill}\t\t|\t\t{self.enemy[3].skill}")
        
            self.name_character = self.all_character[self.index_character][0].name
            print(f"Name: {self.name_character}.")
             
            
            
            for self.my_team_character in self.ally:
                
                if self.name_character in self.my_team_character.name:
                    print("My Team")
                    self.skill_chosse = int(input("Nhập tên Skill: "))
                    self.skill_name = self.all_character[self.index_character][0].skill[self.skill_chosse]
                    print(f"Skill: {self.skill_name}.")
                    
            self.index_character = self.index_character + 1
            
            if self.index_character == 8:
                self.index_character = 0
            
        
    
    def battle_run(self):
        pass
    
    def battle_turn(self):
        for self.index in range(len(self.all_character) - 1):
            for self.index_2 in range( self.index + 1,len(self.all_character)):
                if self.all_character[self.index][1] < self.all_character[self.index_2][1]:
                    self.all_character[self.index], self.all_character[self.index_2] = self.all_character[self.index_2], self.all_character[self.index]
                
        return self.all_character
        
              
my_team = [tanker_01, warriors_01, wizards_01, healer_01]
enermy_team = [tanker_02, warriors_02, ADC_02, healer_02]

my_list = [
    [tanker_01, tanker_01.speed], [warriors_01, warriors_01.speed], [wizards_01, wizards_01.speed],[healer_01, healer_01.speed],
    [tanker_02, tanker_02.speed], [warriors_02, warriors_02.speed], [ADC_02, ADC_02.speed],[healer_02, healer_02.speed]    
]

battle_01 = battle(my_team, enermy_team, my_list)

turn_fight = battle_01.battle_turn()

battle_01.info_battle()


