from ParkingLot import ParkingLot
from datetime import datetime
from Payment import *
from enumerations import *

class Exit:
    def __init__(self, exit_id):
        self.id = exit_id
    
    def validate_ticket(self, ticket):
        if not ticket:
            print("  ✗ No ticket provided")
            return False
        
        lot = ParkingLot.get_instance()
        
        print(f"\n{'─'*60}")
        print(f"  EXIT PANEL #{self.id}".center(60))
        print(f"{'─'*60}")
        print(f"  Ticket #: {ticket.ticket_no}")
        print(f"  Vehicle: {ticket.vehicle.get_type()} {ticket.vehicle.license_no}")
        print(f"  Entry: {ticket.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Set exit time
        ticket.exit_time = datetime.now()
        ticket.exit_ins = self
        
        print(f"  Exit:  {ticket.exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Calculate duration
        duration = ticket.get_duration_hours()
        print(f"  Duration: {duration} hours")
        
        # Calculate fee
        spot = lot.find_spot_by_vehicle(ticket.vehicle)
        if spot:
            ticket.amount = lot.parking_rate.calculate(duration, ticket.vehicle, spot)
            print(f"  Amount: ${ticket.amount}")
            print(f"  Payment: Credit Card")
            
            # Process payment
            payment = CreditCard(ticket.amount, "1234567890123456")
            if payment.initiate_transaction():
                ticket.payment = payment
                ticket.status = TicketStatus.PAID
                
                # Release spot
                spot.remove_vehicle()
                lot.remove_ticket(ticket)
                
                print(f"  ✓ Payment successful. Thank you!")
                print(f"{'─'*60}\n")
                return True
        
        print(f"  ✗ Payment failed")
        print(f"{'─'*60}\n")
        return False