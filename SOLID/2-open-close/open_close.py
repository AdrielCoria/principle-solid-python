'''
Ejercicio
'''

# ----------------------------------------------------------------
#                      GESTIÓN DE FIGURAS GEOMÉTRICAS
# ----------------------------------------------------------------

# class Form:
    
#     # Tenemos que modificar cada una de las funcionalidades cada vez que vienen nuevos
#     # requerimientos
#     def draw_square(self):
#         print("Dibujar un cuadrado")
    
#     def draw_circle(self):
#         print("Dibujar un circulo")
        

class Form:    
    def draw(self):
        pass

class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")
        
class Circle(Form):
    def draw(self):
        print("Dibja un círculo")

class Triangle(Form):
    def draw(self):
        print("Dibuja un triángulo")
        
        
'''
Extra
'''

from abc import ABC, abstractmethod


class Operation():
    
    # Creamos una operación abstracta
    @abstractmethod
    def execute(self, a, b):
        pass
    


