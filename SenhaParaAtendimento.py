def menu():
    import random
    from time import sleep
    for x in range(1):
        menu1 = int(input("Seja bem vindo a Lion Consultoria.\nPara cadastrar seu nome e gerar senha de atendimento pressione '1' e depois a tecla 'Enter'\n"
                          "Caso queira encerrar o atendimento pressione '2': "))
        if menu1 == 1:
            nome = input("Digite seu nome: ")
            num_aleatorio = random.randint(100, 110)
            guiche = random.randint(1, 3)
            print()
            print(f"Olá, Sr(a). {nome}, sua senha é {num_aleatorio}!\nAguarde um pouco que já chamaremos.")
            sleep(10)
            print()
            print(f"Senha: {num_aleatorio}\nSe apresente ao Guichê {guiche}!")
            print()
            menu()
        elif menu1 == 2:
            break
        else:
            print("Número digitado inválido!")
            print()
            menu()

menu()
#função prioridade
#registrar data de entrada e saida
