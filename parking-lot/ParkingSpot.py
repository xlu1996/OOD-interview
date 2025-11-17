from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, spot_id):
        self.id = spot_id
        self.is_free = True
        self.vehicle = None
    
    @abstractmethod
    def assign_vehicle(self, vehicle):
        pass
    
    def remove_vehicle(self):
        if self.vehicle:
            self.vehicle = None
            self.is_free = True
            return True
        return False
    
    def get_type(self):
        return self.__class__.__name__

class Handicapped(ParkingSpot):
    def assign_vehicle(self, vehicle):
        if not self.is_free:
            return False
        self.vehicle = vehicle
        self.is_free = False
        return True

class Compact(ParkingSpot):
    def assign_vehicle(self, vehicle):
        if not self.is_free:
            return False
        if vehicle.get_type() in ['Car', 'Motorcycle']:
            self.vehicle = vehicle
            self.is_free = False
            return True
        return False

class Large(ParkingSpot):
    def assign_vehicle(self, vehicle):
        if not self.is_free:
            return False
        self.vehicle = vehicle
        self.is_free = False
        return True

class MotorcycleSpot(ParkingSpot):
    def assign_vehicle(self, vehicle):
        if not self.is_free:
            return False
        if vehicle.get_type() == 'Motorcycle':
            self.vehicle = vehicle
            self.is_free = False
            return True
        return False