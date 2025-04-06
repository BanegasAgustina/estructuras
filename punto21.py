n=int(input("cuantos triangulos son?: "))
x=0

for i in range(n):
    b=int(input("ingrese base: "))
    a=int(input("ingrese altura: "))

    s=(b*a)/2

    print("superficie",s)

    if s>12:
        x+=1
print("cantidad de triangulos con superficie mayor a 12",x)