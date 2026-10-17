print("Bienvenido")

nombre = input("Ingrese su nombre: ")
producto = input("Ingrese el producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

if subtotal >= 500000:
    descuento = subtotal * 0.15
    total = subtotal - descuento
    print("nombre: ", nombre)
    print("Producto: ", producto)
    print("Subtotal: ", subtotal)
    print("Descuento: ", descuento)
    print("Total a pagar: ", total)
elif subtotal >= 200000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print("nombre: ", nombre)
    print("Producto: ", producto)
    print("Subtotal: ", subtotal)
    print("Descuento: ", descuento)
    print("Total a pagar: ", total)
elif subtotal < 200000:
    descuento = 0
    total = subtotal
    print("nombre: ", nombre)
    print("Producto: ", producto)
    print("Subtotal: ", subtotal)
    print("Total a pagar: ", total)
