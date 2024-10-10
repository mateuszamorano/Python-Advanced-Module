def pir(num):
    for z in range(1, num+1):
        for x in range(1, z+1):
            print(z, end = " ")
        print(f"")
def pir2(num):
    for z in range(1, num+1):
        for x in range(1, z+1):
            print(x, end = " ")
        print(f"")
def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"O texto digitado tem {cont} vogais.")
def inverterNomes(nome1, nome2, nome3, nome4, nome5):
    nomes = [""]*5
    nomes[0]=nome1
    nomes[1]=nome2
    nomes[2]=nome3
    nomes[3]=nome4
    nomes[4]=nome5
    print(nomes)
    nomes.reverse()
    print(nomes)
def somar(numeros):
    t = len(numeros)
    soma=0
    for x in range(t):
        soma = soma + numeros[x]
    print(numeros)

def quant(texto):
    text = input("Insira um texto para saber quantos caractéres tem: ")
