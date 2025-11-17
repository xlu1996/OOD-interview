from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_no):
        self.license_no = license_no
        self.ticket = None
    
    @abstractmethod
    def assign_ticket(self, ticket):
        pass
    
    def get_type(self):
        return self.__class__.__name__

class Car(Vehicle):
    def assign_ticket(self, ticket):
        self.ticket = ticket

class Van(Vehicle):
    def assign_ticket(self, ticket):
        self.ticket = ticket

class Truck(Vehicle):
    def assign_ticket(self, ticket):
        self.ticket = ticket

class Motorcycle(Vehicle):
    def assign_ticket(self, ticket):
        self.ticket = ticket