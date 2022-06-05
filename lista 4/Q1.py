contador=0
num=0
ma= None
me= None
for i in range(100):
    n= int(input("Digite um numero:"))
    contador +=1
    num=num+n
    ma = ma if ma != None and ma >  n else n
    me = me if me != None and me < n else n

media=num/contador    
print(ma)
print(me)
print(media)
    