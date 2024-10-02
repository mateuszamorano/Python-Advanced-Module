def pir(num):
    for z in range(1, num+1):
        for x in range(1, z+1):
            print(z, end = " ")
        print(f"")
num = int(input("Digite um número: "))
pir(num)