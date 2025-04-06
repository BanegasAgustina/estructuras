
v = int(input("Cuántos valores quiere ingresar: "))

for i in range(v):

    x = int(input("ingresar x: "))
    y = int(input("ingresar y: "))


    if x>0 and y>0:
        print("1° cuadrante")
    elif x<0 and y>0:
        print("2° cuadrante")

    elif x<0 and y<0:
        print("3° cuadrante")

    elif x>0 and y<0:
        print("4° cuadrante")
