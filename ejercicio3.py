try:
    with open("archivo1.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no se encuentra. Verifica el nombre del archivo o la ubicación.")