N = ["", "", "", "", ""]
S = ["", "", "", "", ""]
tam = len(N)
cont = 0
opcao = int(input("Bem vindo ao Menu!\n"
                      "Digite '1' para cadastrar ou '2' para login: "))

while opcao == 1 or opcao == 2:
    cont += 3

    if opcao == 2:
        print("Você ainda não fez cadastro! Faça abaixo;")

    for z in range(tam):
        usuario = N[z]
        senha = S[z]
        N[z] = input("Digite o nome dos usuário: ")
        S[z] = input("Digite a senha dos usuário: ")
        print("Usuários cadastrado! Cadastre o próximo;")
    print("Cadastramento finalizado! Siga o próximo passo;")

    usu1 = f"O primeiro usuário: {N[0]}. A senha do mesmo: {S[0]}"
    usu2 = f"O segundo usuário: {N[1]}. A senha do mesmo: {S[1]}"
    usu3 = f"O terceiro usuário: {N[2]}. A senha do mesmo: {S[2]}"
    usu4 = f"O quarto usuário: {N[3]}. A senha do mesmo: {S[3]}"
    usu5 = f"O quinto usuário: {N[4]}. A senha do mesmo: {S[4]}"

    usuario = input("Digite o nome do usuário previamente cadastrado: ")
    senha = input("Digite a senha do usuário previamente cadastrada: ")

    if usuario == N[0] and senha == S[0]:
        print(f"Seja bem vindo Sr(a). {usuario}, login efetuado com sucesso! \nDados cadastrados: "
                  f"{usu1} \n{usu2} \n{usu3} \n{usu4} e \n{usu5}")
    else:
        print("Senha errada, tente novamente!")

    if usuario == N[1] and senha == S[1]:
        print(f"Seja bem vindo Sr(a). {usuario}, login efetuado com sucesso!  \nDados cadastrados: "
                  f"{usu1} \n{usu2} \n{usu3} \n{usu4} e \n{usu5}")
    else:
        print("Senha errada, tente novamente!")

    if usuario == N[2] and senha == S[2]:
        print(f"Seja bem vindo Sr(a). {usuario}, login efetuado com sucesso!  \nDados cadastrados: "
                  f"{usu1} \n{usu2} \n{usu3} \n{usu4} e \n{usu5}")
    else:
        print("Senha errada, tente novamente!")

    if usuario == N[3] and senha == S[3]:
        print(f"Seja bem vindo Sr(a). {usuario}, login efetuado com sucesso! \nDados cadastrados: "
                  f"{usu1} \n{usu2} \n{usu3} \n{usu4} e \n{usu5}")
    else:
        print("Senha errada, tente novamente!")

    if usuario == N[4] and senha == S[4]:
        print(f"Seja bem vindo Sr(a). {usuario}, login efetuado com sucesso! \nDados cadastrados: "
                  f"{usu1} \n{usu2} \n{usu3} \n{usu4} e \n{usu5}")
    else:
        print("Senha errada, tente novamente!")

    proc = int(input("Deseja encerrar o sistema? Se sim, pressione a tecla '1', caso contrário pressione '2': "))
    if proc == 1:
        break
