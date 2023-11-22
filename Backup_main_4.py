def exibir_submenu(submenu):
    print("Opções do submenu:")
    for key, value in submenu.items():
        print(f"{key}. {value}")

def calcular_formula(valor1, valor2):
    try:
        resultado = (valor1 - valor2) / valor2 * (100)
        return resultado
    except ZeroDivisionError:
        print("Erro: O segundo valor não pode ser igual a zero.")
        return None
def calcular_taxa_pulverizacao():
    try:
        # Solicitar ao usuário os três números
        vazao_por_bico = float(input("Digite a vazão por bico (litros por minuto): "))
        faixa_pulverizacao_por_bico = float(input("Digite a faixa de pulverização por bico (metros): "))
        velocidade_trabalho = float(input("Digite a velocidade de trabalho (quilômetros por hora): "))

        # Calcular a taxa de pulverização
        taxa_pulverizacao = (vazao_por_bico * 600) / (faixa_pulverizacao_por_bico * velocidade_trabalho)

        # Imprimir o resultado
        print(f"A taxa de pulverização é: {taxa_pulverizacao:.2f} litros por hectare.")
    except ValueError:
        print("Erro: Digite apenas números válidos.")
def submenu_opcao_2():
    print("Você escolheu a opção 2.")
    submenu = {
        "a": "Patinamento",
        "b": "Avanço",
        "c": "Lastragem",
        "d": "Voltar"
    }
    while True:
        exibir_submenu(submenu)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu:
            if escolha_submenu == "d":
                break
            elif escolha_submenu == "c":
                print("Você escolheu a opção 'Lastragem'.")
                submenu_lastragem = {
                    "a": "Duplagem",
                    "b": "Voltar"
                }
                while True:
                    exibir_submenu(submenu_lastragem)
                    escolha_lastragem = input("Escolha uma opção do submenu: ").lower()
                    if escolha_lastragem in submenu_lastragem:
                        if escolha_lastragem == "b":
                            break
                        print(f"Você escolheu {submenu_lastragem[escolha_lastragem]}.")
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print(f"Você escolheu {submenu[escolha_submenu]}.")
        else:
            print("Opção inválida. Tente novamente.")

def submenu_opcao_3():
    print("Você escolheu a opção 3. Acesse o submenu para mais opções.")
    submenu = {
        "a": "Dimensionamento da potência útil do trator",
        "b": "Potência necessária para tracionar um equipamento",
        "c": "Voltar"
    }
    while True:
        exibir_submenu(submenu)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu:
            if escolha_submenu == "c":
                break
            print(f"Você escolheu {submenu[escolha_submenu]}.")
        else:
            print("Opção inválida. Tente novamente.")

def submenu_opcao_4():
    print("Você escolheu a opção 4.")
    submenu = {
        "a": "Desempenho operacional prático",
        "b": "Desempenho operacional teórico",
        "c": "Voltar"
    }
    while True:
        exibir_submenu(submenu)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu:
            if escolha_submenu == "c":
                break
            elif escolha_submenu == "b":
                print("Você escolheu a opção 'Desempenho operacional teórico'.")
                submenu_teorico = {
                    "a": "Comparativo entre tratores",
                    "b": "Voltar"
                }
                while True:
                    exibir_submenu(submenu_teorico)
                    escolha_teorico = input("Escolha uma opção do submenu: ").lower()
                    if escolha_teorico in submenu_teorico:
                        if escolha_teorico == "b":
                            break
                        print(f"Você escolheu {submenu_teorico[escolha_teorico]}.")
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print(f"Você escolheu {submenu[escolha_submenu]}.")
        else:
            print("Opção inválida. Tente novamente.")

def submenu_opcao_5():
    print("Você escolheu a opção 5.")
    submenu = {
        "a": "Pulverizadores",
        "b": "Semeadoras",
        "c": "Distribuidor de corretivos",
        "d": "Voltar",
    }
    while True:
        exibir_submenu(submenu)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu:
            if escolha_submenu == "d":
                break
            elif escolha_submenu in ["a", "b", "c"]:
                print(f"Você escolheu {submenu[escolha_submenu]}.")
                # Implemente a lógica do submenu específico aqui, para cada equipamento.
                # Por exemplo, se escolha_submenu == "a", é o submenu para "Pulverizadores".
                # Implemente o código para a opção "Pulverizadores" aqui.
                # Você pode criar uma função específica para cada equipamento, se necessário.
                # Exemplo para a opção "Pulverizadores":
                if escolha_submenu == "a":
                    submenu_pulverizadores()
                elif escolha_submenu == "b":
                    submenu_semeadoras()
                elif escolha_submenu == "c":
                    submenu_distribuidor_corretivos()
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

# Funções para os submenus específicos de cada equipamento em "Opção 5".
def submenu_pulverizadores():
    print("Você escolheu a opção 'Pulverizadores'.")
    submenu_pulverizadores = {
        "a": "Características do pulverizador",
        "b": "Quantidade do produto",
        "c": "Voltar"

    }
    while True:
        exibir_submenu(submenu_pulverizadores)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu_pulverizadores:
            if escolha_submenu == "c":
                break
            print(f"Você escolheu {submenu_pulverizadores[escolha_submenu]}.")
            # Implemente a lógica para cada opção específica do submenu de "Pulverizadores" aqui.
            if escolha_submenu == "a":
                calcular_taxa_pulverizacao()
            elif escolha_submenu == "b":
                opcao_modelo_2_pulverizador()

        else:
            print("Opção inválida. Tente novamente.")



def submenu_semeadoras():
    print("Você escolheu a opção 'Semeadoras'.")
    # Implemente a lógica do submenu de "Semeadoras" aqui, se necessário.
    pass

def submenu_distribuidor_corretivos():
    print("Você escolheu a opção 'Distribuidor de corretivos'.")
    # Implemente a lógica do submenu de "Distribuidor de corretivos" aqui, se necessário.
    pass



def submenu_opcao_6():
    print("Você escolheu a opção 6.")
    submenu = {
        "a": "Estimativa de potência",
        "b": "Características dimensionais",
        "c": "Cálculo do comprimento da correia",
        "d": "Reserva de torque",
        "e": "Teoria da tração",  # Corrigindo o nome da opção
        "f": "Voltar"
    }
    while True:
        exibir_submenu(submenu)
        escolha_submenu = input("Escolha uma opção do submenu: ").lower()
        if escolha_submenu in submenu:
            if escolha_submenu == "f":
                break
            elif escolha_submenu == "d":
                try:
                    valor1 = float(input("Digite o primeiro valor (Torque máximo): "))
                    valor2 = float(input("Digite o segundo valor (Torque na potência máxima: "))
                    resultado = calcular_formula(valor1, valor2)
                    if resultado is not None:
                        print(f"O resultado da reserva de torque é: {resultado:.2f}")
                except ValueError:
                    print("Erro: Digite apenas números válidos.")
            else:
                print(f"Você escolheu {submenu[escolha_submenu]}.")
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    menu = {
        "1": "Custos trator e equipamentos.",
        "2": "Adequação.",
        "3": "Dimensionamento trator e equipamento.",
        "4": "Desempenho operacional e comparativos.",
        "5": "Adequação de equipamentos.",
        "6": "Características dimensionais.",
        "7": "Sair"  # Adicionando uma opção para sair do programa
    }

    while True:
        print("\nMenu Principal:")
        for key, value in menu.items():
            print(f"{key}. {value}")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Você escolheu a opção 1.")
            # Implemente a lógica do submenu da opção 1 aqui, se necessário.
            pass
        elif escolha == "2":
            submenu_opcao_2()
        elif escolha == "3":
            submenu_opcao_3()
        elif escolha == "4":
            submenu_opcao_4()
        elif escolha == "5":
            submenu_opcao_5()
        elif escolha == "6":
            submenu_opcao_6()
        elif escolha == "7":
            print("Você escolheu sair. Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
menu_principal()
