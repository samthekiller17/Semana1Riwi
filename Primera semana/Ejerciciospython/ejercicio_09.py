print("Bienvenido")

compra=float(input("precio de la compra: "))

if compra >= 200000:
    descuento=compra*0.20
    total=compra-descuento
    print(f"El precio de la compra es: {compra}, el descuento es: {descuento}, el total a pagar es: {total}")
elif compra >= 100000:
    descuento=compra*0.10
    total=compra-descuento
    print(f"El precio de la compra es: {compra}, el descuento es: {descuento}, el total a pagar es: {total}")
else:
    print(f"El precio de la compra es: {compra}, no hay descuento, el total a pagar es: {compra}")
