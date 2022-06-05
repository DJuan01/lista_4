contador=0
quant_1=0
quant_2=0
quant_3=0
quant_4=0
quant_5=0
for i in range(3):
    idade= int(input("Digite um numero:"))
    if idade<15:
        quant_1=quant_1+1
        contador +=1
    elif 16<=idade<=30:
        quant_2=quant_2+1
        contador +=1
    elif 31<=idade<=45:
        quant_3=quant_3+1
        contador +=1
    elif 46<=idade<=60:
        quant_4=quant_4+1
        contador +=1
    elif idade>60:
        quant_5=quant_5+1
        contador +=1
por_1=quant_1/contador
por_2=quant_5/contador
print(quant_1)
print(quant_2)
print(quant_3)
print(quant_4)
print(quant_5)
print(por_1)
print(por_2)