class Weapon():
    def __init__(self, name, type, damage, recharge):
        self.name = name
        self.type = type
        self.damage = damage
        self.recharge = recharge
class Person():
    def __init__(self, playername, playerhealth, playerattack, playerattack2):
        self.name = playername
        self.attack1 = playerattack
        self.attack2 = playerattack2
        self.health = playerhealth