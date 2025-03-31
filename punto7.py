x=int(input("ingrese eje x:"))
y=int(input("ingrese eje y:"))

if x>0 and y>0:
    print("1° cuadrante")
elif x<0 and y>0:
    print("2° cuadrante")

elif x<0 and y<0:
    print("3° cuadrante")

elif x>0 and y<0:
    print("4° cuadrante")
