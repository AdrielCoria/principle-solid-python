'''
Ejercicio
'''

from abc import ABC, abstractmethod
# abstract basic class

# FORMA INCORRECTA
# class WorkerInterface(ABC):


#     @abstractmethod
#     def work(self):
#         pass
    
    
#     @abstractmethod
#     def eat(self):
#         pass


# class Human(WorkerInterface):
#     def work(self):
#         print("Trabajando")
    
    
#     def eat(self):
#         print("Comiendo")
    
    
# class Robot(WorkerInterface):
#     def work(self):
#         return super().work()
    
#     def eat(self): # El robot no puede comer <--
#         pass
        
        
# human = Human()
# human.work()
# human.eat()        
        
# robot = Robot()
# robot.work()
# robot.eat() # El robot no puede comer -> Es un problema de diseño


# FORMA CORRECTA

class WorkerInterface(ABC):


    @abstractmethod
    def work(self):
        pass


class EatInterface(ABC):


    @abstractmethod
    def eat(self):
        pass

class Human(WorkerInterface, EatInterface):
    def work(self):
        print("Trabajando")
    
    
    def eat(self):
        print("Comiendo")
    
    
class Robot(WorkerInterface):
    def work(self):
        return super().work()


human = Human()
human.work()
human.eat()        
        
robot = Robot()
robot.work()
   
'''
Extra
'''

class PrinterInterface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass

class ColorPrinterInterface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document: str) -> str:
        pass

class FaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass

class Printer(PrinterInterface):
    def print(self, document):
        print(f"Imprimiendo en blanco y negro el documento {document}.")
    

class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document):
        print(f"Imprimiendo a color el documento {document}.")
        

class MultifunctionPrinter(ColorPrinterInterface, ScannerInterface, FaxInterface, PrinterInterface):
    def print_color(self, document):
        print(f"Escaneando el documento {document}.")
        return f"Document {document} escaneado."
    
    
    def scan(self, document):
        print(f"Escaneando el documento {document}.")
        return f"Document {document} escaneado."
    
    
    def send_fax(self, document):
        print(f"Escaneando el documento {document}.")
        return f"Document {document} escaneado."
    
    
    def print(self, document):
        print(f"Imprimiendo en blanco y negro el documento {document}.")
        return f"Document {document} escaneado."
    
    
def test_printer():
    
    printer = Printer()
    color_printer = ColorPrinter()
    multifunction_printer = MultifunctionPrinter()
    
    printer.print("doc.pdf")
    color_printer.print_color("doc.pdf")
    
    # Esta impresora hace todo
    multifunction_printer.print("doc.pdf")
    multifunction_printer.print_color("doc.pdf")
    multifunction_printer.send_fax("doc.pdf")
    multifunction_printer.scan("doc.pdf")
    
test_printer()
    