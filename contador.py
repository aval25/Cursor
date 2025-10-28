# Programa para contar las palabras de un archivo de texto
from collections import Counter
from hashlib import blake2b
import re

class ContadorDePalabras:
    """Clase para contar palabras en archivos de texto."""
    
    def __init__(self):
        self.contenido = ""
        self.palabras = []
        self.frecuencias = Counter()
    
    def leer_archivo(self, ruta):
        """
        Lee el contenido de un archivo de texto.
        
        Args:
            ruta (str): Ruta del archivo a leer
            
        Returns:
            str: Contenido del archivo
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            IOError: Si hay un error al leer el archivo
        """
        # Lista de encodings comunes a probar
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'utf-16']
        
        for encoding in encodings:
            try:
                with open(ruta, "r", encoding=encoding) as archivo:
                    self.contenido = archivo.read()
                print(f"Archivo leído correctamente con encoding: {encoding}")
                return self.contenido
            except UnicodeDecodeError:
                continue
            except FileNotFoundError:
                raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
            except IOError as e:
                raise IOError(f"Error al leer el archivo: {e}")
        
        # Si ningún encoding funcionó, intentar con 'errors=ignore'
        try:
            with open(ruta, "r", encoding="utf-8", errors="ignore") as archivo:
                self.contenido = archivo.read()
            print("Archivo leído con encoding UTF-8 ignorando caracteres problemáticos")
            return self.contenido
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        except IOError as e:
            raise IOError(f"Error al leer el archivo: {e}")
    
    def contar_palabras(self):
        """
        Cuenta las palabras en el contenido del archivo.
        
        Returns:
            tuple: (total_palabras, frecuencias_top10)
                - total_palabras: número total de palabras
                - frecuencias_top10: lista de las 10 palabras más frecuentes
        """
        if not self.contenido:
            raise ValueError("No hay contenido para procesar. Use leer_archivo() primero.")
        
        # Separar las palabras usando expresión regular
        self.palabras = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', self.contenido.lower())
        
        # Contar número total de palabras
        total_palabras = len(self.palabras)
        
        # Calcular frecuencias
        self.frecuencias = Counter(self.palabras)
        frecuencias_top10 = self.frecuencias.most_common(10)
        
        return total_palabras, frecuencias_top10
    
    def mostrar_resultados(self, total_palabras, frecuencias_top10):
        """
        Muestra los resultados del conteo de palabras.
        
        Args:
            total_palabras (int): Total de palabras encontradas
            frecuencias_top10 (list): Lista de las 10 palabras más frecuentes
        """
        print(f"\nTotal de palabras encontradas: {total_palabras}")
        print("\nLas 10 palabras más frecuentes y su conteo:")
        for palabra, conteo in frecuencias_top10:
            print(f"{palabra}: {conteo}")


def main():
    """Función principal para ejecutar el programa."""
    contador = ContadorDePalabras()
    
    # Pedir al usuario la ruta del archivo
    ruta = input("Ingrese la ruta del archivo de texto: ")
    
    try:
        # Leer el archivo
        contador.leer_archivo(ruta)
        
        # Contar las palabras
        total_palabras, frecuencias_top10 = contador.contar_palabras()
        
        # Mostrar resultados
        contador.mostrar_resultados(total_palabras, frecuencias_top10)
        
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


# Test para la clase ContadorDePalabras
def test_contador_palabras():
    """Test básico para verificar el funcionamiento de la clase."""
    contador = ContadorDePalabras()
    
    # Crear un archivo de prueba temporal
    contenido_prueba = "hola mundo hola python mundo hola"
    with open("archivo_prueba.txt", "w", encoding="utf-8") as f:
        f.write(contenido_prueba)
    
    try:
        contador.leer_archivo("archivo_prueba.txt")
        total, frecuencias = contador.contar_palabras()
        
        # Verificar que cuenta correctamente
        assert total == 6, f"Esperado 6 palabras, obtenido {total}"
        assert frecuencias[0][0] == "hola", f"Primera palabra más frecuente debería ser 'hola', obtenido {frecuencias[0][0]}"
        assert frecuencias[0][1] == 3, f"'hola' debería aparecer 3 veces, obtenido {frecuencias[0][1]}"
        
        print("✓ Test pasado correctamente")
        
    finally:
        # Limpiar archivo de prueba
        import os
        if os.path.exists("archivo_prueba.txt"):
            os.remove("archivo_prueba.txt")


# Descomentar la siguiente línea para ejecutar el test
# test_contador_palabras()