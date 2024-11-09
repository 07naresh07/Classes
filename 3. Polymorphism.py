class vehicle:
    def __init__(self, name, brand):
        self.name=name
        self.brand=brand
class car(vehicle):
        
    def movement(self):
        print("Drive!!")
        
class boat(vehicle):
    
    def movement(self):
        print("Sail!!")
        
class plane(vehicle):
    
    def movement(self):
        print("Fly")
        
m = car("Car", "Toyota")
n = boat("Ship", "Titanic")
o = plane("Aeroplane", "Nepal Airlines")


for x in(m, n, o):
    x.movement()
    print(x.name)
    print(x.brand)


    
        
