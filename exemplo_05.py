def calcular_area():
    tipo = input("Você quer calcular a área de um quadrado ou de um retângulo? (quadrado/retângulo): ").strip().lower()

    if tipo == "quadrado":
        lado = float(input("Informe o comprimento do lado do quadrado: "))
        area = lado * lado
        print(f"A área do quadrado é: {area} unidades quadradas.")
    elif tipo == "retângulo":
        comprimento = float(input("Informe o comprimento do retângulo: "))
        largura = float(input("Informe a largura do retângulo: "))
        area = comprimento * largura
        print(f"A área do retângulo é: {area} unidades quadradas.")
    else:
        print("Opção inválida. Por favor, escolha entre 'quadrado' ou 'retângulo'.")

calcular_area()
