n1 = int(input("Ingrese primer valor:"))
n2 = int(input("Ingrese segundo valor:"))
n3 = int(input("Ingrese tercer valor:"))

if n1 < n2 and n1 < n3:
    print(n1)
else:
    if n2 < n3:
        print(n2)
    else:
        print(n3)

if n1 > n2 and n1 > n3:
    print(n1)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)
