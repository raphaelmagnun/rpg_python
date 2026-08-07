class Character:
    #Construtor:
    def __init__(self, name:str, max_life:int, attack_power:int, defense:int):
        self.name = name
        self.max_life = max_life
        self.life = max_life
        self.attack_power = attack_power
        self.defense= defense

    def is_alive(self) -> bool:
        return self.life > 0

    def take_damage(self, damage: int) -> int:
        real_damage = max(0, damage - self.defense)
        self.life = max (0, self.life - real_damage)
        return real_damage
        
        #Usa-se aspas no Character pois a classe Caracter ainda não foi criada até essa linha
    def attack (self, target: "Character") -> int:
        return target.take_damage(self.attack_power)