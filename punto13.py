tp= int(input("Ingrese total de preguntas:"))
tr= int(input("Ingrese respuestas corresctas:"))

p=tp*100/tr

if p>= 90:
    print("nivel maximo")
else:
    if p>=75:
         print("nivel medio")
    else:
        if p >= 50:
             print("nivel regular")
        else:
             print("fuera de nivel")