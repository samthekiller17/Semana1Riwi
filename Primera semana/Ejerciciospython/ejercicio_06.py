print("Bienvenido")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es {resultado}.")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es {resultado}.")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es {resultado}.")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"La división de {numero1} y {numero2} es {resultado}.")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operación no válida.")