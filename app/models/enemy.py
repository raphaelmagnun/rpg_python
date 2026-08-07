from app.models.personagem import Character

class Enemy(Character):
    def __init__ (
            self,
            name: str,
            max_life: int,
            attack_power: int,
            defense: int,
            exp_reward: int,
            ):
              #Pai (super), inicia os parametros (nome, maxlife...) pra mim.
             super().__init__(name, max_life, attack_power, defense)

             self.exp_reward = exp_reward
    