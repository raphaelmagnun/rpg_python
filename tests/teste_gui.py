# O que cada linha faz?
# import tkinter as tk: Importamos a biblioteca e damos o apelido curto tk (convenção padrão no Python).
# janela = tk.Tk(): Instancia a janela principal.
# janela.geometry("400x300"): Define 400 pixels de largura por 300 de altura (atenção: usa a letra x entre os números).
# janela.mainloop(): Fundamental! Sem essa linha, a janela abre e fecha em um milissegundo. 
# Ela congela a execução do Python ali, escutando cliques e eventos até você fechar a janela.


import tkinter as tk

janela = tk.Tk()
janela.title("Criação de Personagem")
janela.geometry("400x250")

# 1. Rótulo de instrução
label_instrucao = tk.Label(
    janela,
    text="Digite o nome do seu herói:",
    font=("Arial", 12)
)
label_instrucao.pack(pady=5)

# 2. Campo de Entrada (Entry)
caixa_nome = tk.Entry(
    janela,
    font=("Arial",12)
)
caixa_nome.pack(pady=5)

label_pontos_vida = tk.Label(
    janela, 
    text="Digite os pontos de vida inicial:",
    font=("Arial", 12)
)
label_pontos_vida.pack(pady=5)

caixa_vida = tk.Entry(
    janela,
    font=("Arial",12)
)
caixa_vida.pack(pady=5)

# 3. Rótulo onde exibiremos o resultado (inicia sem texto)
label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial",12, "bold"),
    fg="blue"
)
label_resultado.pack(pady=10)

# 4. Função executada quando o botão for clicado
def confirmar_nome():
  nome = caixa_nome.get().strip()

  try:
    # Tenta converter o texto da vida para número inteiro
    vida = int(caixa_vida.get().strip())

    if nome:
      label_resultado.config(text=f"Herói: {nome} | Vida: {vida} HP")
    else:
      label_resultado.config(text="Digite um nome válido!")

  except ValueError:
    # Caso a conversão falhe (usuário digitou letras ou deixou em branco)
    label_resultado.config(text="Erro: A vida deve ser um número inteiro!")

botao_confirma = tk.Button(
    janela,
    text="Confirmar",
    command=confirmar_nome
    )
botao_confirma.pack(pady=5)

janela.mainloop()