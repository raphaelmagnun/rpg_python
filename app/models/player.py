from app.models.personagem import Character
    
class Player(Character): #A classe Player herda da classe Character
    def __init__ (
            self,
            name: str,
            max_life: int,
            attack_power: int,
            defense: int,
            ):    

            #Mas para herdar os atributos preciso usar o método super() "pai"
            super().__init__(name, max_life, attack_power, defense)      
            
            self.level = 1
            self.exp = 0
            self.exp_next_level = 50

    def level_up(self):
        self.exp -= self.exp_next_level  #30 = 30-20  = exp = 10
        self.level += 1 #GANHA 1 LEVEL 1+1 = level = 2
        self.exp_next_level = int(self.exp_next_level * 1.1) 

        #Bônus por subir nível:
        self.max_life += 20
        self.attack_power += 5
        self.defense +=2
        self.life = self.max_life

    def gain_exp(self, amount:int):   #amout 30
        self.exp += amount #exp = 30
        while self.exp >= self.exp_next_level:
            self.level_up()