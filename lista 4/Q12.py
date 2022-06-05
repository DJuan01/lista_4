n = int(input('Digite o número de linhas: '))
impar=-1
par=0
for i in range( n ):
    
    impar+=2
    print(impar, end="")
print()
for i in range(n):
    par+=2
    print(par, end="")