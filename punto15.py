n = int(input("Ingrese la cantidad de alturas a ingresar: "))
sa = 0
i = 1

while i <= n:
    altura = float(input("Ingrese altura: "))
    sa += altura
    i += 1

prom = sa / n
print("Altura promedio:", prom)
