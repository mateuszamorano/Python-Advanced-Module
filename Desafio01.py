N = [""]*5
S = [""]*5
tam = len(N)
cont1 = 0
cont2 = 0
menu = 0

while menu != 4 and cont1 == 0:

    menu = int(input("Menu: \n1 - Cadastro \n2 - Login \n3 - Mostrar Dados \n4 - Sair \nEscolha: "))

    if menu == 4:
        print("Sistema finalizado!")
        break

    if menu == 1:
        for z in range(tam):
            N[z] = input("Cadastre o nome dos usuário: ")
            S[z] = input("Cadastre a senha dos usuário: ")
            print("Usuário cadastrado! Cadastre o próximo;")
        print("Cadastramento finalizado! Siga o próximo passo;")

    elif menu == 2:
        log = input("Digite o seu usuário: ")
        for x in range(tam):
            if log == N[x]:
                sen = input("Digite a sua senha: ")
                if sen == S[x]:
                    print("Login efetuado com sucesso!")
                    cont1 += 1
                while sen != S[x] and cont2 < 2:
                    sen = input(f"Você errou a senha, digite-a novamente: ")
                    cont2 += 1
                    if cont2 == 2 and sen != S[x]:
                        print("Sistema encerrado por senhas erradas!")
                        cont1 += 1
                    elif sen == S[x]:
                        print("Login efetuado com sucesso!")
                        cont1 += 1
        if log not in N:
            print("Usuário não cadastrado! Escolha novamente uma opção; ")

    elif menu == 3:
        print(f"Usuários em ordem: {N}, \n  Senhas em ordem: {S}")
print(f"Usuários em ordem: {N} \n  Senhas em ordem: {S}")
