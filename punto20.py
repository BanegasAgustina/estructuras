n = int(input("Cuántos valores quiere ingresar: "))
i = 0
p = 0
im = 0

while i < n:
    v = int(input("Ingrese un valor: "))
    if v % 2 == 0:
        p += 1
    else:
        im += 1
    i += 1  

print("Hay", p, "números pares y", im, "números impares")
