# Pede o nome do usuário
nome = print("Qual seu nome? ")  # print() exibe algo no ecrã, mas aqui só imprime, não armazena
nome = input()  # input() lê o que o usuário digita e guarda na variável 'nome'

# Saudação usando f-string
print(f"Olá {nome}, seja bem-vindo à calculadora!")  
# f-string permite inserir valores de variáveis dentro de strings: {nome}

# Constante Pi
P = 3.141592653589793  # número Pi aproximado

# Lista para guardar o histórico de operações
historico = []  # [] cria uma lista vazia

# Definição de função para ler números
def ler_numero(mensagem):  # def define uma função chamada 'ler_numero' que recebe um parâmetro 'mensagem'
    while True:  # loop infinito que só termina com 'return' (ou break)
        valor = input(mensagem)  # lê a entrada do usuário
        if valor.strip().upper() == "P":  
            # .strip() remove espaços antes/depois
            # .upper() transforma tudo em maiúsculas
            return P  # return devolve o valor P para quem chamou a função
        try:  
            # try tenta executar algo que pode dar erro
            return float(valor)  # converte a string digitada para número decimal
        except ValueError:  
            # except captura o erro específico 'ValueError' (quando a conversão falha)
            print(f"{nome}, valor inválido! Tente novamente.")  

# Função para mostrar menu de operações
def mostrar_menu():  
    print(
        "\nEscolha a operação desejada:\n"
        "1) + para soma\n"
        "2) - para subtração\n"
        "3) * para multiplicação\n"
        "4) / para divisão\n"
        "5) r para raiz\n"
        "6) % para resto da divisão\n"
        "7) // para divisão inteira\n"
    )

# Função para calcular as operações
def calcular(x, operação, y):  
    if operação == "+":  
        z = x + y  # operador de adição
        print(f"{nome}, a soma de {x} + {y} é igual a {z}")
    elif operação == "-":  
        z = x - y  # subtração
        print(f"{nome}, a subtração de {x} - {y} é igual a {z}")
    elif operação == "*":  
        z = x * y  # multiplicação
        print(f"{nome}, a multiplicação de {x} * {y} é igual a {z}")
    elif operação == "/":  
        if y == 0:  
            # Verifica divisão por zero
            print(f"{nome}, não é possível dividir por zero!")
            return None  # return None indica que não há resultado válido
        z = x / y  # divisão normal
        print(f"{nome}, a divisão de {x} / {y} é igual a {z}")
    elif operação == "r":  
        if y == 0:  
            print(f"{nome}, não é possível calcular raiz de índice zero!")
            return None
        z = x ** (1/y)  # raiz y de x
        print(f"{nome}, a raiz {y} de {x} é igual a {z}")  
    elif operação == "%":  
        z = x % y  # resto da divisão
        print(f"{nome}, o resto da divisão de {x} % {y} é igual a {z}")
    elif operação == "//":  
        z = x // y  # divisão inteira
        print(f"{nome}, a divisão inteira de {x} // {y} é igual a {z}")    
    else:
        print(f"Desculpe {nome}. Mas, a operação é inválida!")
        return None
    historico.append(f"{x} {operação} {y} = {z}")  
    # adiciona operação realizada na lista 'historico'
    return z  # devolve o resultado da operação

# Loop principal do programa
while True:  
    x = ler_numero("Digite o primeiro número (ou P para Pi): ")  # chama função para ler número
    mostrar_menu()  # mostra menu de operações
    operação = input("Digite o símbolo da operação que deseja fazer: ")  # lê operação
    y = ler_numero("Digite o segundo número (ou P para Pi): ")  # lê segundo número

    z = calcular(x, operação, y)  # calcula e guarda resultado

    if z is not None:  # se resultado válido
        ver_hist = input("Deseja ver o histórico de operações? (s/n): ").lower()  
        # .lower() transforma em minúscula
        if ver_hist == "s":
            print("Histórico de operações:")
            print("\n".join(historico))  
            # "\n".join(lista) junta todos os elementos da lista com quebra de linha

    while z is not None:  # loop para continuar com resultado anterior
        adicionar = input("Deseja adicionar outra operação ao resultado? (s/n): ").lower()
        if adicionar == "s":
            x = z  # usa resultado anterior como novo x
            mostrar_menu()
            operação = input("Digite o símbolo da operação que deseja fazer: ")
            y = ler_numero("Digite o segundo número (ou P para Pi): ")
            z = calcular(x, operação, y)
            if z is not None:
                ver_hist = input("Deseja ver o histórico de operações? (s/n): ").lower()
                if ver_hist == "s":
                    print("Histórico de operações:")
                    print("\n".join(historico))
        else:
            break  # sai do loop se não quiser continuar

    repetir = input("Deseja fazer um novo cálculo? (s/n) (n ira fechar o programa!): ").lower()
    if repetir != "s":  # se não digitar 's', encerra
        print(f"Obrigado, {nome}, por usar a calculadora do Tripa <3!")
        break  # termina o loop principal, encerrando o programa