def menu():
    import random
    from time import sleep
    for x in range(1):
        menu1 = int(input("Seja bem vindo ao Lion Consultoria.\nPara cadastrar seu nome e gerar senha de atendimento, pressione '1' e depois a tecla 'Enter': "))
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
        else:
            print("Número digitado inválido!")
            menu()
menu()