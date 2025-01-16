class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        
    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.calcular_subtotal()}"