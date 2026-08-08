from app.models import Player, Enemy, Combate

# 1. Instanciamos o Herói e o Inimigo
heroi = Player("Raphael", max_life=50, attack_power=15, defense=3)
monstro = Enemy("Goblin", max_life=30, attack_power=8, defense=2, exp_reward=120)

# 2. Criamos a arena de combate
batalha = Combate(enemy=monstro, player=heroi)

print(f"⚔️ Um {monstro.name} apareceu!\n")

# 3. Loop de combate rodando enquanto a luta não for encerrada
while not batalha.luta_encerrada:
    print(f"--- SEU TURNO ---")
    print(f"HP {heroi.name}: {heroi.life}/{heroi.max_life} | HP {monstro.name}: {monstro.life}/{monstro.max_life}")
    escolha = input("Escolha: [1] Atacar | [2] Fugir: ")
    
    # Executa a ação do jogador
    batalha.executar_turno_jogador(escolha)
    
    # Verifica se o inimigo morreu antes dele responder
    batalha.verificar_vencedor()
    
    # Se a luta não acabou, o inimigo ataca de volta
    if not batalha.luta_encerrada:
        print(f"\n--- TURNO DO INIMIGO ---")
        batalha.executar_turno_inimigo()
        batalha.verificar_vencedor()
        print("-" * 30 + "\n")

# 4. Resultado final
print("\n=== FIM DA BATALHA ===")
if heroi.is_alive() and not monstro.is_alive():
    print(f"🏆 Vitória! {heroi.name} venceu a batalha!")
    print(f"Nível atual: {heroi.level} | XP atual: {heroi.exp}/{heroi.exp_next_level}")
elif not heroi.is_alive():
    print(f"💀 Game Over! {heroi.name} foi derrotado...")
else:
    print(f"🏃 {heroi.name} fugiu do combate!")