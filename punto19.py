l1 =0
l2=0

i=0

while i<=15:
    n = int(input("Ingrese valores:"))
    l1+=n
    i+=1

i=0
print("segunda lista")

while i<=15:
    n = int(input("Ingrese valores:"))
    l2+=n
    i+=1
if l1 < l2:
    print("la lista1 es menor a lista2")
elif l1 > l2 :
    print("lista1 es mayor a lista2")
else:
    print("las dos listas son iguales")