dig = ["", "", "", "", ""]
soma = 0
cont = 0

tam = len(dig)
for z in range(tam):
    dig[z] = float(input("Digite as notas dos alunos: "))

for x in range(tam):
    soma = soma + dig[x]
    media = soma / tam

for c in range(tam):
    if dig[c] > media:
        cont+=1

print(f"Temos {cont} com a nota maior que a média que foi: {media} ")