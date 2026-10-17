print("Bienvenido")

n=int(input("Ingrese un número: "))
suma=0

for i in range(n+1):
    suma += i

print(f"La suma de los numeros de {n} es: {suma}")