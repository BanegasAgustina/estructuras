# Inicializamos contadores
equilateros = 0
isoceles = 0
escalenos = 0

n = int(input("Ingrese la cantidad de triángulos: "))

for i in range(1, n + 1):
    print(f"\nTriángulo {i}:")
    lado1 = float(input("Ingrese el lado 1: "))
    lado2 = float(input("Ingrese el lado 2: "))
    lado3 = float(input("Ingrese el lado 3: "))

    
    if lado1 == lado2 == lado3:
        print("Es un triángulo equilátero.")
        equilateros += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles.")
        isoceles += 1
    else:
        print("Es un triángulo escaleno.")
        escalenos += 1


print("\nResumen:")
print("Cantidad de triángulos equiláteros:", equilateros)
print("Cantidad de triángulos isósceles:", isoceles)
print("Cantidad de triángulos escalenos:", escalenos)
