
# 1) Solicita ao usuário que digite seu nome

try:
    nome = input("Digite seu nome: ")

    if len(nome) == 0:
        raise ValueError("Nome não pode estar vazio")
        exit()

    elif any(char.isdigit() for char in nome):
        raise ValueError("Tem números junto ao nome")
        exit()

    else:
        print("Nome válido")
    
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite o valor do seu bonus: "))

# 4) Calcule o valor do bônus final

BONUS_2024 = 1000
bonus_final = BONUS_2024 + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O funcionário(a) {nome} tem um salário de R${salario:.2f}. Recebeu um bonus final de R${bonus_final:.2f} ")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?