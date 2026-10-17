print("Bienvenido a verificar tu edad.")

nombre=input("Por favor, ingresa tu nombre: ")
edad=int(input("Por favor, ingresa tu edad: "))
print(f"Hola, {nombre}. Tienes {edad} años.")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

