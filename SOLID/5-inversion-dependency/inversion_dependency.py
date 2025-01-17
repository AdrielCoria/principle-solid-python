'''
Ejercicio: Botón de una lámpara y switch
'''

# FORMA INCORRECTA -> Esta muy acomplado -> Si el switch es para un TV

# Bajo Nivel
# class Switch:
    
#     def turn_on(self):
#         print("Enciende la lámpara")
    
    
#     def turn_off(self):
#         print("Apaga la lámpara")
        
# # Alto Nivel
# class Lamp:
    
#     def __init__(self):
#         self.switch = Switch()
        
#     def operate(self, command):
#         if command == "on":
#             self.switch.turn_on()
        
#         elif command == "off":
#             self.switch.turn_off()
            
# lamp = Lamp()
# lamp.operate("on")
# lamp.operate("off")

# FORMA CORRECTA
class ISwitch:
    
    def turn_on(self):
       pass
    
    
    def turn_off(self):
        pass
        
class LampSwitch(ISwitch):
    
    def turn_on(self):
        print("Enciende la lámpara")
    
    def turn_off(self):
        print("Apaga la lámpara")
        
class Lamp:
    
    def __init__(self, switch: ISwitch) -> None:
        self.switch = switch
        
    def operate(self, command):
        if command == "on":
            self.switch.turn_on()
        
        elif command == "off":
            self.switch.turn_off()


lamp = Lamp(LampSwitch())
lamp.operate("on")
lamp.operate("off")            


'''
Extra
'''
from abc import ABC, abstractmethod


class Notifier(ABC):
    
    def send(self, message: str):
        pass
    
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Enviando email con texto: {message}")

class PushNotifier(Notifier):
    def send(self, message):
        print(f"Enviando PUSH con texto: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Enviando SMS con texto: {message}")
        
        
class NotificationService:
    
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    
    def notify(self, message: str):
        self.notifier.send(message)
        

# service = NotificationService(EmailNotifier())
# service = NotificationService(PushNotifier())
service = NotificationService(SMSNotifier())
service.notify("Hola, notificador!!")


