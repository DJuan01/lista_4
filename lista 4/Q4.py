par=0
impar=0
for i in range(100):
    n= int(input("Digite um numero:"))
    if n%2==0:
        par=par+n
    else:
        impar=impar+n

print(par)
print(impar)
    
