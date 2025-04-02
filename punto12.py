n= int(input("Ingrese segundo valor:"))

if n < 10:
    print("el numero ",n,"es de 1 cifra")
elif n<100:
    print("el numero ",n,"es de 2 cifras")
elif n<1000:
    print("el numero ",n,"es de 3 cifras")
else:
    
    print("el numero ",n,"es de 4 cifras o mas")
    