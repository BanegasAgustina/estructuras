m=0
my=0
g=0
i=1

n = int(input("Ingrese la cantidad de empleados: "))

while i<=n:
    s= float(input("Ingrese sueldo: "))

    if s<=300:
        m+=1
    else:
        my+=1
    g=g+s
    i+=1



print("gasto de empresa en sueldos: ",g)
print("empleados que cobran menos que 300",m)
print("empleados que cobran mas de 300",my)
