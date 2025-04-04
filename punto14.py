m = 0   
my = 0  
i = 1

while i <=10:
    n = int(input("Ingrese la nota: "))
    if n >= 7:
        my += 1
    else:
        m += 1
    i += 1  # esto hace que se avance al siguiente 

print("Los que tienen notas mayores o iguales a siete son:", my)
print("Los que tienen notas menores a siete son:", m)
