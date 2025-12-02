def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + dado2
    print("Resultado da concatenação:", resultado)


def repetir_texto():
    texto = input("Digite um texto: ")
    vezes = int(input("Digite o número de repetições: "))
    print(texto * vezes)


def operacoes_matematicas():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Operação (+, -, *, /): ")

    if operacao == "+":
        print("Resultado:", n1 + n2)
    elif operacao == "-":
        print("Resultado:", n1 - n2)
    elif operacao == "*":
        print("Resultado:", n1 * n2)
    elif operacao == "/":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero não permitida.")
    else:
        print("Operação inválida.")


def verificar_par_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")


def calcular_media():
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    media = (n1 + n2 + n3) / 3
    print("Média:", media)


def verificar_palindromo():
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")


def menu():
    while True:
        print("\n====== DESAFIOS PYTHON COM GITHUB COPILOT ======")
        print("1 - Concatenar dados")
        print("2 - Repetir textos")
        print("3 - Operações matemáticas")
        print("4 - Verificar par ou ímpar")
        print("5 - Calcular média de notas")
        print("6 - Verificar palíndromo")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            concatenar_dados()
        elif escolha == "2":
            repetir_texto()
        elif escolha == "3":
            operacoes_matematicas()
        elif escolha == "4":
            verificar_par_impar()
        elif escolha == "5":
            calcular_media()
        elif escolha == "6":
            verificar_palindromo()
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Inicia o programa
menu()
