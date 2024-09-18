# Solicita ao usuário que insira o sexo
sexo = input("Digite o sexo (M/F): ").upper()

# Verifica se o valor inserido é válido
while sexo != "M" and sexo != "F":
    print("Valor inválido! Por favor, digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Digite o sexo (M/F): ").upper()

# Exibe o valor inserido
print("Sexo inserido:", sexo)
