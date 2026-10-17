print("Bienvenido")

print("Cajero")

saldo = 500000

consultar_saldo= saldo
retirar_dinero = 0
depositar_dinero = 0
salir= False

usuario = input("Que quieres hacer? (consultar saldo, retirar dinero, depositar dinero, salir): ")

if usuario == "consultar saldo":
    print("Tu saldo es: ", consultar_saldo)
elif usuario == "retirar dinero":
    retirar_dinero = int(input("Cuanto dinero quieres retirar?: "))
    if retirar_dinero > saldo:
        print("No tienes suficiente saldo")
    else:
        saldo -= retirar_dinero
        print("Tu nuevo saldo es: ", saldo)
elif usuario == "depositar dinero":
    depositar_dinero = int(input("Cuanto dinero quieres depositar?: "))
    saldo += depositar_dinero
    print("Tu nuevo saldo es: ", saldo)
elif usuario == "salir":
    salir = True
