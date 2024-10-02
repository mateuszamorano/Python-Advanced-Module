N = ["", "", "", "", ""]
S = ["", "", "", "", ""]
tam = len(N)


opcao = input("Bem vindo ao Menu!\n"
              "Digite '1' para cadastrar ou '2' para login: ")

if opcao != 1 and opcao != 2:

for z in range(tam):

    N[z] = input("Digite o nome dos usuário: ")
    S[z] = input("Digite a senha dos usuário: ")

while opcao == 1:

    if login == N[0] and senha == S[0]:
        print("Você entrou com sucesso!")
    elif login == N[1] and senha == S[1]:
        print("Você entrou com sucesso!")
    elif login == N[2] and senha == S[2]:
        print("Você entrou com sucesso!")
    elif login == N[3] and senha == S[3]:
        print("Você entrou com sucesso!")
    elif login == N[4] and senha == S[4]:
        print("Você entrou com sucesso!")
    else:
        print("Login ou senha inseridos está errado!")

print(F"O primeiro usuário: {N[0]}. A senha do mesmo: {S[0]}"
      F"\nO segundo usuário: {N[1]}. A senha do mesmo: {S[1]}"
      F"\nO terceiro usuário: {N[2]}. A senha do mesmo: {S[2]}"
      F"\nO quarto usuário: {N[3]}. A senha do mesmo: {S[3]}"
      F"\nO quinto usuário: {N[4]}. A senha do mesmo: {S[4]}")
