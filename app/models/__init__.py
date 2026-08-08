from app.models.personagem import Character
from app.models.player import Player
from app.models.enemy import Enemy
from app.models.combate import Combate


#O __all__ avisa ao python que o Character, Player e Enemy são exportações propositais da pasta models.

__all__ = ["Character", "Player", "Enemy", "Combate"]