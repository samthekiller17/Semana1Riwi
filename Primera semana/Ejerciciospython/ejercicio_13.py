print("Bienvenido")

numero1 = int(input("Por favor, ingresa el primer número: "))
numero2 = int(input("Por favor, ingresa el segundo número: "))

print("Menu de operaciones")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
operacion = input("Ingresa 1 si quieres sumar, 2 si quieres restar, 3 si quieres multiplicar, 4 si quieres dividir: ")


if operacion == "1":
    resultado = numero1 + numero2
elif operacion == "2":
    resultado = numero1 - numero2
elif operacion == "3":
    resultado = numero1 * numero2
elif operacion == "4":
    resultado = numero1 / numero2 if numero2 != 0 else "No se puede dividir entre cero"
else:
    resultado = "Operación no válida"

print(f"La operación seleccionada es: {operacion}. El resultado es: {resultado}.")