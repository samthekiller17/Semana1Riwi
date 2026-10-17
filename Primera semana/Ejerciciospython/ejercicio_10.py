print("Bienvenido")

usuario="Samuel"
contraseña="1234"

peticion_usuario=input("Ingrese su usuario: ")
peticion_contraseña=input("Ingrese su contraseña: ")

if peticion_usuario==usuario and peticion_contraseña==contraseña:
    print("Bienvenido al sistema.")
else:
    print("Usuario o contraseña incorrectos.")