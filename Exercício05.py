N = ["", "", "", "", ""]
S = ["", "", "", "", ""]
tam = len(N)
for z in range(tam):
    N[z] = input("Digite o nome dos usuários: ")
    S[z] = input("Digite a senha dos usuários: ")
print(F"O primeiro usuário: {N[0]}. A senha do mesmo: {S[0]}"
      F"\nO segundo usuário: {N[1]}. A senha do mesmo: {S[1]}"
      F"\nO terceiro usuário: {N[2]}. A senha do mesmo: {S[2]}"
      F"\nO quarto usuário: {N[3]}. A senha do mesmo: {S[3]}"
      F"\nO quinto usuário: {N[4]}. A senha do mesmo: {S[4]}")