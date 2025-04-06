
s1 = 0  
s2 = 0  
s3 = 0  

for i in range(5):
    e = int(input("Ingrese la edad del estudiante del turno mañana: "))
    s1 += e
p1 = s1 / 5
print("Promedio edades turno mañana (tm):", p1)


for i in range(6):
    e2 = int(input("Ingrese la edad del estudiante del turno tarde: "))
    s2 += e2
p2 = s2 / 6
print("Promedio edades turno tarde (tt):", p2)


for i in range(11):
    e3 = int(input("Ingrese la edad del estudiante del turno noche: "))
    s3 += e3
p3 = s3 / 11
print("Promedio edades turno noche (tn):", p3)

if p1 > p2 and p1 > p3:
    print("El tm tiene el promedio de edades mayor.")
elif p2 > p3:
    print("El tt tiene el promedio de edades mayor.")
else:
    print("El tn tiene el promedio de edades mayor.")
