print("Bienvenido")

temperatura=float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 10:
    print(f"La temperatura es {temperatura}°C, hace frío.")
elif temperatura >= 10 and temperatura <= 25:
    print(f"La temperatura es {temperatura}°C, hace un clima temblada.")
elif temperatura >= 25 and temperatura <= 35:
    print(f"La temperatura es {temperatura}°C, hace calor.")
else:
    print(f"La temperatura es {temperatura}°C, hace mucho calor.")