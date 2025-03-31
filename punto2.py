n1=int(input("ingrese primera nota:"))
n2=int(input("ingrese segunda nota:"))
n3=int(input("ingrese tercera nota:"))

promedio = (n1+n2+n3)/3

if promedio > 7:
    print("promocionado")
else:
    print("reprobado")