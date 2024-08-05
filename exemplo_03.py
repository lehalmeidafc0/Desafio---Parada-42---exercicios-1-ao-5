# Definindo a estrutura de dados para armazenar as informações dos produtos
produtos = []

# Função para cadastrar um produto
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    
    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    
    produtos.append(produto)

# Cadastrando dois produtos
for _ in range(2):
    cadastrar_produto()

# Exibindo as informações dos produtos cadastrados e o valor total das compras
valor_total = 0

print("\nInformações dos produtos cadastrados:")
for produto in produtos:
    print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")
    valor_total += produto['quantidade'] * produto['preco']

print(f"\nValor total das compras: R$ {valor_total:.2f}")
