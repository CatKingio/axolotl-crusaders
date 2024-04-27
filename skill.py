class skill:
    def __init__(self, name, damage, mana, cooldown):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.cooldown = cooldown

class effect(skill):
    def __init__(self, name, damage, mana, cooldown):
        super().__init__(name, damage, mana, cooldown)
        pass
