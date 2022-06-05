contador=0
quant_1=0
quant_2=0
quant_3=0
idade_1=0
idade_2=0
idade_3=0

for i in range(3):
    idade= int(input("Digite a sua idade:"))
    av= int(input("Digite sua avaliacao do filme 1:regular;2:bom;3otimo:"))
    
    if av==1:
        idade_1= idade_1+ idade
        quant_1 +=1
        contador +=1
    elif av==2:
        idade_2= idade_2+ idade
        quant_2 +=1
        contador +=1
    elif av==3:
        idade_3= idade_3+ idade
        quant_3=quant_3+1
        contador +=1
if quant_3>0:        
    media_3=idade_3/quant_3
    print(media_3)
else:
    print("0")
porc_2=quant_2/contador
print(quant_1)
print(porc_2)