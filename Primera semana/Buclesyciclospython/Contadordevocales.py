print("Bienvenido")

Texto=input("Ingrese un texto: ")

vocales=0
for letra in Texto:
    if letra.lower() in "aeiou":
        vocales += 1

print("vocales: ", vocales)