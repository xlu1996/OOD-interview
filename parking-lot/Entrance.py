from enumerations import TicketStatus
from ParkingTicket import ParkingTicket
from ParkingLot import ParkingLot
class Entrance:
    def __init__(self, entrance_id):
        self.id = entrance_id
    
    def get_ticket(self, vehicle):
        lot = ParkingLot.get_instance()
        
        # Find available spot
        available_spot = lot.find_available_spot(vehicle)
        if not available_spot:
            print(f"  ✗ Parking lot is FULL. Cannot admit {vehicle.get_type()} {vehicle.license_no}")
            return None
        
        # Create ticket
        ticket = ParkingTicket(vehicle, self)
        ticket.status = TicketStatus.IN_USE
        
        # Assign spot
        if available_spot.assign_vehicle(vehicle):
            vehicle.assign_ticket(ticket)
            lot.add_ticket(ticket)
            print(f"  ✓ {vehicle.get_type()} {vehicle.license_no} assigned ticket #{ticket.ticket_no}")
            print(f"    Parked in {available_spot.get_type()} spot #{available_spot.id}")
            return ticket
        
        return None