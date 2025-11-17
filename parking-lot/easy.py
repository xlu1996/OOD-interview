"""
PARKING LOT DESIGN QUESTION
A parking lot or car park is a dedicated cleared area that is intended for parking vehicles. In most countries where cars are a major mode of transportation, parking lots are a feature of every city and suburban area. Shopping malls, sports stadiums, megachurches, and similar venues often feature parking lots over large areas.



We will focus on the following set of requirements while designing the parking lot:
SYSTEM REQUIREMENTS:
The parking lot should have multiple floors where customers can park their cars.
The parking lot should have multiple entry and exit points.
Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points on their way out.
Customers can pay the tickets at the automated exit panel or to the parking attendant.
Customers can pay via both cash and credit cards.
Customers should also be able to pay the parking fee at the customer’s info portal on each floor. If the customer has paid at the info portal, they don’t have to pay at the exit.
The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.
Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Handicapped, Motorcycle, etc.
The Parking lot should have some parking spots specified for electric cars. These spots should have an electric panel through which customers can pay and charge their vehicles.
The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.
Each parking floor should have a display board showing any free parking spot for each spot type.
The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.

big parkiing lot
4 entrances - 4 exits
ticket and spot allocated at entrance
parking spot should be nearest to the entrance
limit of cars allowed - 30k
parking spot types - Handy cap, compact, large, motocycle
cash and credit
there should be a monitoring system

classes/objects in system:
vehicle (bus, card, motorcycle)
parking lot system (level - with a parking spot class)
entry/exit terminals (printers, payment processes)
parking spot
ticket
database
monitoring system
------------------------

The parking lot should have multiple levels, each level with a certain number of parking spots.
The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
Each parking spot should be able to accommodate a specific type of vehicle.
The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
The system should track the availability of parking spots and provide real-time information to customers.
The system should handle multiple entry and exit points and support concurrent access.

"""
from abc import ABC
from enum import Enum

# abc is abstract bae class -> is a class that should not be instantiated directly
# it is meant to be inherited by subclasses that implement its behaviour
class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    TRUCK = 3


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.type = vehicle_type

    def get_type(self) -> VehicleType:
        return self.type

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)
class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.TRUCK)

class Level:
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots = [ParkingSpot(i) for i in range(num_spots)]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else "Occupied"}")

class ParkingSpot:
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.vehicle_type = VehicleType.CAR
        self.parked_vehicle = None
    def is_available(self) -> bool:
        return self.parked_vehicle is None
    def park_vehicle(self, vehicle) -> None:
        if self.is_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot is already occupied")
        
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle
    def get_spot_number(self) -> int:
        return self.spot_number

class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._intance = self
            self.levels = []
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, level: Level) -> None:
        self.levels.append(level)
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()


class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))

        car = Car("ABC1234")
        truck = Truck("XYZ789")
        motorcycle = Motorcycle("M1234")

        # park the vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehuicle(motorcycle)

        # display availability
        parking_lot.display_availability()

        # unpark vehicle
        parking_lot.unpark_vehicle(motorcycle)

        # display updated availability
        parking_lot.disply_availability()

if __name__ == "__main__":
        ParkingLotDemo.run()