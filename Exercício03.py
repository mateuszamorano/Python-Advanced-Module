A = [0,0,0,0,0,0,0,0,0,0]
x = 0
M = [0,0,0,0,0,0,0,0,0,0]
tam = len(A)

for z in range(tam):

    A[z]=int(input("Digite o número: "))
x = int(input("Digite o multiplicador: "))

for c in range(tam):
    M[x]=A[c]*x

print(A)
print(x)
print(M)