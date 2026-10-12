class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class bike(vehicle):
    def __init__(self,brand,model,fuel_cost):
        super().__init__(brand,model) #initalizing the parent class/vehicle part
        self.fuel_cost=fuel_cost #initializing car specific part
    def fuel_cost(self):
        return self.fuel_cost
brand = input("Enter the bikes brand: ")
model = input("Enter the bikes model: ")
fuel_cost = int(input("Enter the fuel cost: "))
bike1 = bike(brand,model,fuel_cost)
print(f"{bike1.brand} is of {bike1.model}model and its fuel cost: {bike1.fuel_cost}")