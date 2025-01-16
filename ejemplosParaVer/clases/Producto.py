class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, precio={self.precio})"
    