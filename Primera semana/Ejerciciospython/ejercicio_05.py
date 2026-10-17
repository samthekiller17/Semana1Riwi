print("Bienvenido")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
else:
    if numero1 == numero2:
        print(f"Los números {numero1} y {numero2} son iguales.")
    else:
        print(f"El número {numero2} es mayor que {numero1}.")