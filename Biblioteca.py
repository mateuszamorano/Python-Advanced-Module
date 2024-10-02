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
