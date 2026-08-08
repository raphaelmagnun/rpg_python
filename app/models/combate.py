from app.models.enemy import Enemy
from app.models.player import Player

class Combate:
    def __init__(self, enemy: Enemy, player: Player):
        self.enemy = enemy
        self.player = player
        self.luta_encerrada = False

    def executar_turno_jogador(self, acao):
        if int(acao) == 1:
            self.player.attack(self.enemy)
        elif int(acao) == 2:
            self.luta_encerrada = True

    def executar_turno_inimigo(self):
        if self.enemy.life > 0:
            self.enemy.attack(self.player)

    def verificar_vencedor(self):
        if not self.enemy.is_alive():
            self.player.gain_exp(self.enemy.exp_reward)
            
        if not self.enemy.is_alive() or not self.player.is_alive():
            self.luta_encerrada = True  
