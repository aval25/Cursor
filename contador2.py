from collections import Counter
import re
ruta = input("Ingrese la ruta del archivo de texto: ")

 # 2- Leer el contenido del archivo
with open(ruta, "r") as archivo:
    contenido = archivo.read()

 # 3- separar las palabras
palabras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', contenido)

 # 4- contar numero total de palabras
total_palabras = len(palabras)

 # 5- Mostrar las 10 palabras más frecuentes y su conteo
frecuencias = Counter(palabras)
frecuencias_top10 = frecuencias.most_common(10)
print("Las 10 palabras más frecuentes y su conteo:")
for palabra, conteo in frecuencias_top10:
    print(f"{palabra}: {conteo}")