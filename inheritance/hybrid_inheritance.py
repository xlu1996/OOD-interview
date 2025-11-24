# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_info(self):
        print(f"Brand: {self.brand}")

# First branch - Fuel Car
class FuelCar(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type
    
    def refuel(self):
        print(f"Refueling with {self.fuel_type}")

# Second branch - Electric Car
class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity
    
    def recharge(self):
        print(f"Recharging {self.battery_capacity}kWh battery")

# Hybrid inherits from BOTH FuelCar and ElectricCar
class HybridCar(FuelCar, ElectricCar):
    def __init__(self, brand, fuel_type, battery_capacity):
        # Initialize both parent classes
        FuelCar.__init__(self, brand, fuel_type)
        ElectricCar.__init__(self, brand, battery_capacity)
    
    def switch_mode(self, mode):
        if mode == "fuel":
            print("Switched to fuel mode")
        elif mode == "electric":
            print("Switched to electric mode")

# Usage
print("--- Fuel Car ---")
fuel_car = FuelCar("Toyota", "Petrol")
fuel_car.show_info()
fuel_car.refuel()

print("\n--- Electric Car ---")
electric_car = ElectricCar("Tesla", 100)
electric_car.show_info()
electric_car.recharge()

print("\n--- Hybrid Car ---")
hybrid_car = HybridCar("Toyota Prius", "Petrol", 50)
hybrid_car.show_info()
hybrid_car.refuel()
hybrid_car.recharge()
hybrid_car.switch_mode("electric")