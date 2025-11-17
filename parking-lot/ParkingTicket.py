from enum import Enum, auto
from abc import ABC, abstractmethod
from datetime import datetime
from Payment import *
from enumerations import *

class ParkingTicket:
    _ticket_counter = 1000
    
    def __init__(self, vehicle, entrance):
        ParkingTicket._ticket_counter += 1
        self.ticket_no = ParkingTicket._ticket_counter
        self.entry_time = datetime.now()
        self.exit_time = None
        self.amount = 0.0
        self.status = TicketStatus.ISSUED
        
        self.vehicle = vehicle
        self.payment = None
        self.entrance = entrance
        self.exit_ins = None
    
    def get_duration_hours(self):
        if self.exit_time:
            duration = (self.exit_time - self.entry_time).total_seconds() / 3600
        else:
            duration = (datetime.now() - self.entry_time).total_seconds() / 3600
        return round(duration, 2)
