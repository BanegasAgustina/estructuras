s = int(input("Ingrese sueldo: "))
a = int(input("Ingrese años de antigüedad: "))

if s < 500 and a >= 10:
    print("Se le otorga un aumento del 20%")
    s += s * 0.20 
    print(f"El sueldo es: ${s:.2f}")

elif s < 500 and a < 10:
    print("Se le otorga un aumento del 5%")
    s += s * 0.05
    print(f"El sueldo es: ${s:.2f}")

elif s >= 500:
    print(f"El sueldo es: ${s:.2f}")
