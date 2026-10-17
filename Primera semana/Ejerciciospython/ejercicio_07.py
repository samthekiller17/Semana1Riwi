print("Bienvenido")

edad=float(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad.")
elif edad < 0:
    print("La edad ingresada no es válida.")
else:
    print("Usted es menor de edad.")