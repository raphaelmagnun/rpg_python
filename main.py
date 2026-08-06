from app.models.personagem import Character

heroi = Character("Raphael", 100, 20, 50)
monstro = Character("Gollum", 60, 10, 10)

print(f"--- ESTADO INICIAL ---")
print(f"{heroi.name}: {heroi.life}/{heroi.max_life} HP")
print(f"{monstro.name}: {monstro.life}/{monstro.max_life} HP\n")

dano_causado = heroi.attack(monstro)

# 4. Exibimos os resultados da ação
print(f"--- AÇÃO DE ATAQUE ---")
print(f"⚔️ {heroi.name} atacou {monstro.name} causando {dano_causado} de dano real!")
print(f"Vida atual de {monstro.name}: {monstro.life}/{monstro.max_life} HP")
print(f"{monstro.name} está vivo? {monstro.is_alive()}\n")

# 5. Simulando um ataque fatal para testar a trava de vida em zero
print(f"--- SEGUNDO ATAQUE (FATAL) ---")
dano_causado_2 = heroi.attack(monstro)
print(f"⚔️ {heroi.name} atacou {monstro.name} novamente causando {dano_causado_2} de dano!")
print(f"Vida final de {monstro.name}: {monstro.life}/{monstro.max_life} HP")
print(f"{monstro.name} está vivo? {monstro.is_alive()}")