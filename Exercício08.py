N = [0]*10
tam = len(N)
num = 0
cont = 0

for z in range(tam):
    N[z] = int(input("Digite um número: "))

num1 = int(input("Digite o número pra saber quantas vezes ele foi digitado anteriormente: "))

for x in range(tam):
    if num1 == N[x]:
        cont += 1
print(f"Este número apareceu {cont} vezes!.")