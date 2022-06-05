n=int(input("Digite um numero entre 1000 e 1999:"))
i=1
for i in range(i):
        if n<1000 or n>1999:
            print("Numero fora do intervalo")
            
        elif 1000<=n<=1999:
            if n%11==5:
                print("Esse numero tem resto 5")
                break
            else:
                print("esse numero nao tem resto 5")
                break
print("reinicei e tente outro numero")