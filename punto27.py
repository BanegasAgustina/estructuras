n=0
p=0
m15=0
sp=0
for i in range(11):
    v = int(input("ingresar numeros: "))
    if v<0:
        n+=1
    else:
        p+=1
    if v%15==0:
        m15+=1
    if v%2==0:
        sp=sp+v
print("numeros negativos: ",n)
print("numeros positivos: ",p)
print("numeros multiplos de 15:",m15)
print("suma de numeros pares : ",sp)

    