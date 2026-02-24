#crear una clase llamada libro con atributos titulo, autor y páginas

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

#implementar métodos accesadores 

    def get_titulo(self):
        return self.titulo 
    
    def get_autor(self):
        return self.autor
    
    def get_paginas(self):
        return self.paginas
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_autor(self, autor):
        self.autor = autor
        
    def set_paginas(self, paginas):
        self.paginas = paginas

#relacion de colaboración crear una clase llamada Biblioteca que tenga un atributo

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro) 

    def mostrar_libro(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(f"- {libro.get_titulo()}")
        
    
#relacion de composición crear una clase llamado estante y que tenga un atributo llamado libros (lista de objetos de la clase libro)

class Estante:
    def __init__(self):
        self.libros = [] 
    
    # AGREGAR 'libro' AQUÍ:
    def agregar_libro(self, libro): 
        self.libros.append(libro)
    
    def mostrar_libro(self):
        print("Libros en el estante:")
        for libro in self.libros:
            print(f"- {libro.get_titulo()}")
        
#probar el código

Libro1 = Libro("El principito", "Antoine de Saint-Exupery", 200)
Libro2 = Libro("El gran Gatsby", "F.Scott Fitzgerald", 180) 

#crear un objeto de clase biblioteca y agregar los libros a la biblioteca

Mi_biblioteca = Biblioteca() 

Mi_biblioteca.mostrar_libro() 
#crear un objeto llamado estante y agregar los libros al estante

mi_estante = Estante()

mi_estante.mostrar_libro()

#llamar a los métodos mostrar_libros() en ambos objetos para verificar que los libros se agregaron

Biblioteca.mostrar_libro(Libro1)
Biblioteca.mostrar_libro(Libro2)

Estante.mostrar_libro(Libro1)
Estante.mostrar_libro(Libro2)

print("Libros en la biblioteca:")
Mi_biblioteca.mostrar_libro() 

print("Libros en el estante:")
mi_estante.mostrar_libro()    # <--- Llama al objeto, no a la clase


# 1. Creación de la Clase Principal: Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Atributos inicializados mediante el constructor
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas

    # Métodos Accesores (Getters)
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_paginas(self):
        return self._paginas

    # Métodos Mutadores (Setters)
    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self._autor = nuevo_autor

    def set_paginas(self, nuevas_paginas):
        self._paginas = nuevas_paginas


# 2. Relación de Colaboración: Biblioteca
class Biblioteca:
    def __init__(self):
        # Atributo libros: una lista vacía para almacenar objetos Libro
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado a la Biblioteca.")

    def mostrar_libros(self):
        print("\n--- Libros en la Biblioteca ---")
        for libro in self.libros:
            print(f"Título: {libro.get_titulo()} | Autor: {libro.get_autor()}")


# 3. Relación de Composición: Estante
class Estante:
    def __init__(self):
        # Atributo libros: lista de objetos Libro
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' colocado en el Estante.")

    def mostrar_libros(self):
        print("\n--- Libros en el Estante ---")
        for libro in self.libros:
            print(f"Título: {libro.get_titulo()} | Autor: {libro.get_autor()}")


# 4. Prueba el Código
if __name__ == "__main__":
    # Crear al menos dos objetos de la clase Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 471)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
    libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1000)
    libro4 = Libro("Rayuela", "Julio Cortázar", 600)
   
    # Crear objeto de la clase Biblioteca y agregar libros
    mi_biblioteca = Biblioteca()
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)
    
    

    # Crear objeto de la clase Estante y agregar libros
    mi_estante = Estante()
    mi_estante.agregar_libro(libro1)
    mi_estante.agregar_libro(libro2)
    mi_estante.agregar_libro(libro3)
    mi_estante.agregar_libro(libro4)
    

    # Verificar funcionalidad llamando a mostrar_libros()
    mi_biblioteca.mostrar_libros()
    mi_estante.mostrar_libros()