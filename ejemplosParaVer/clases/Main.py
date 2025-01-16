from Producto import Producto
from DetalleVenta import DetalleVenta
from Venta import Venta

# Creamos productos
producto1 = Producto(1, "Lapiz", 1000)
producto2 = Producto(2, "Regla", 1500)
producto3 = Producto(3, "Goma", 500)

# Creamos el detalle de la venta
detalle1 = DetalleVenta(producto1, 3) # 3 Lapices
detalle2 = DetalleVenta(producto2, 2) # 2 Reglas
detalle3 = DetalleVenta(producto3, 4) # 4 Gomas

# Total = 3000 + 3000 + 2000 = 8.000

# Creamos una venta con sus detalles de venta
ventaUtiles = Venta()
ventaUtiles.agregar_detalle(detalle1)
ventaUtiles.agregar_detalle(detalle2)
ventaUtiles.agregar_detalle(detalle3)

# Mostramos la venta hecha
ventaUtiles.mostrar_venta()


