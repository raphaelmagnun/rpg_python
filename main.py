from app.models import Player, Enemy

# 1. Criamos os personagens
heroi = Player(name="Raphael", max_life=100, attack_power=25, defense=5)
goblin = Enemy(
    name="Goblin Saqueador",
    max_life=30,
    attack_power=10,
    defense=2,
    exp_reward=110,
)

print(f"--- INÍCIO DO COMBATE ---")
print(f"{heroi.name} (Nível {heroi.level}) vs {goblin.name}\n")

# 2. O herói ataca o goblin
dano = heroi.attack(goblin)
print(f"⚔️ {heroi.name} causou {dano} de dano no {goblin.name}!")
print(f"Vida do {goblin.name}: {goblin.life}/{goblin.max_life}\n")

# 3. O herói desfere um segundo golpe (fatal)
dano = heroi.attack(goblin)
print(f"⚔️ {heroi.name} causou {dano} de dano no {goblin.name}!")
print(f"{goblin.name} está vivo? {goblin.is_alive()}\n")

# 4. Se o inimigo morreu, o herói recebe a recompensa de XP do monstro
if not goblin.is_alive():
  print(f"💀 {goblin.name} foi derrotado!")
  print(f"✨ {heroi.name} recebeu {goblin.exp_reward} de XP!\n")
  heroi.gain_exp(goblin.exp_reward)

# 5. Exibimos o status final do jogador após o combate
print(f"--- STATUS FINAL DO JOGADOR ---")
print(f"Nível: {heroi.level}")
print(f"XP: {heroi.exp}/{heroi.exp_next_level}")
print(f"HP Max: {heroi.max_life}")
print(f"Ataque: {heroi.attack_power}")