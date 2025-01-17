'''
Ejercicio
'''

# Animalitos -> Aves

# INCORRECTO
# class Bird:
#     def fly(self):
#         return "Flying"

# class Chicken(Bird):
#     def fly(self):
#         raise Exception("Los pollos no vuelan!!!")
    
    
# bird = Bird()
# bird.fly()

# chicken = Chicken()
# chicken.fly()

# CORRECTA
class Bird:
    def move(self):
        return "Moving"
    
class Chicken(Bird):
    def move(self):
        return "Walk"

bird = Bird()
print(bird.move())

chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())

chicken = Bird()
print(chicken.move())
    
    
'''
Extra
'''  

class Vehicle:
    
    def __init__(self, speed=0):
        self.speed = speed
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")
    
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed  <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")
        

class Car(Vehicle):
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)    
    
    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)
    
class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("La bicicleta está acelerando")
        super().accelerate(increment)    
    
    def brake(self, decrement):
        print("La bicicleta está frenando")
        super().brake(decrement)

class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La motocicleta está acelerando")
        super().accelerate(increment)    
    
    def brake(self, decrement):
        print("La motocicleta está frenando")
        super().brake(decrement)

# Probamos...
def text_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)

car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

text_vehicle(car)
text_vehicle(bicycle)
text_vehicle(motorcycle)


