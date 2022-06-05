par=0
impar=0
i=1
while i>0:
    n= int(input("Digite um numero:"))
    if 1<=n<=500:
        if n%2==0:
            ...
        else:
            impar=impar+n
    else:
        break
print(impar)
    