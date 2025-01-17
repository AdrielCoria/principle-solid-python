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
    
class Addition():
    def execute(self, a, b):
        return a + b
    
    
class Subtration():
    def execute(self, a, b):
        return a - b
    
    
class Multiplicate():
    def execute(self, a, b):
        return a * b
    
    
class Division():
    def execute(self, a, b):
        return a / b
    
class Power():
    def execute(self, a, b):
        return a ** b
    

class Calculator(): 
    def __init__(self):
        self.operations = {}
        
    def add_operation(self, name, operation):
        self.operations[name] = operation
        
    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)
            
    

calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("subtration", Subtration())
calculator.add_operation("multiplicate", Multiplicate())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())


print(calculator.calculate("addition", 10, 2))
print(calculator.calculate("subtration", 10, 2))
print(calculator.calculate("multiplicate", 10, 2))
print(calculator.calculate("division", 10, 2))
print(calculator.calculate("power", 10, 2))
