nombres = []
while True:
    nombre = input("Ingrese un nombre (o escriba 'fin' para salir): ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Los nombres han sido escritos en el archivo 'nombres.txt'.")