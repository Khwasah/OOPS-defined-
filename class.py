'''
Inheritance: Vehicle → Car, Bike, 
each with a different fuel_cost().
'''


class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class car(vehicle):
    def __init__(self,brand,model,fuel_cost):
        super().__init__(brand,model) #initalizing the parent class/vehicle part
        self.fuel_cost=fuel_cost #initializing car specific part
    def fuel_cost(self):
        return self.fuel_cost
brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
fuel_cost = int(input("Enter the fuel cost: "))
car1 = car(brand,model,fuel_cost)
print(f"{car1.brand} is of {car1.model}model and its fuel cost: {car1.fuel_cost}")