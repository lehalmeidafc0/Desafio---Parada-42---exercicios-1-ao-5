def cadastrar_usuario():
    # Coletando dados do usuário
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    
    # Exibindo os dados cadastrados
    print("\nDados cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")

# Executando a função de cadastro
cadastrar_usuario()
