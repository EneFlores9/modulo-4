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
