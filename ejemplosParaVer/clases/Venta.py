from datetime import datetime

class Venta:
    def __init__(self, fecha=None):
        self.fecha = fecha if fecha else datetime.now()
        self.detalle_venta = [] # Lista para almacenar los detalles de las ventas
        
    def agregar_detalle(self, detalle):
        self.detalle_venta.append(detalle)
        
    def calcular_total(self):
        return sum(detalle.calcular_subtotal() for detalle in self.detalle_venta)
    
    def mostrar_venta(self):
        print(f"Fecha: {self.fecha}")
        print("Detalle de la venta")
        
        for detalle in self.detalle_venta:
            print(f"{detalle}")
        print(f"Total: {self.calcular_total()}")
        