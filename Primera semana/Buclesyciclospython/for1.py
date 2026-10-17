aprobado = 0
notas=[2.5, 3.0, 4.5, 1.0, 5.0, 2.0, 3.5]
for nota in notas:
    if nota >= 3.0:
        aprobado += 1
print("Cantidad de aprobados: ", aprobado)