n = int(input("Digite um número qualquer: "))
valor = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        valor += 1
        print( valor, end=" ")
    print( )
    valor = 0