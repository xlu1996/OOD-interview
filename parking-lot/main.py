import time
from Vehicle import Car, Van, Motorcycle, Truck
from ParkingSpot import Handicapped, Compact, Large, MotorcycleSpot
from ParkingLot import ParkingLot
from DisplayBoard import DisplayBoard
from Entrance import Entrance
from Exit import Exit

def main():
    print("\n" + "="*70)
    print("  PARKING LOT SYSTEM DEMO".center(70))
    print("="*70 + "\n")

    # Reset singleton for fresh start
    ParkingLot.reset_instance()
    
    # Initialize parking lot
    lot = ParkingLot.get_instance()
    lot.add_spot(Handicapped(1))
    lot.add_spot(Compact(2))
    lot.add_spot(Large(3))
    lot.add_spot(MotorcycleSpot(4))

    # Add display board
    board = DisplayBoard(1)
    lot.add_display_board(board)

    # Add entrance and exit
    entrance = Entrance(1)
    exit_panel = Exit(1)

    # SCENARIO 1: CUSTOMER ENTERS AND PARKS
    print("\n" + "▶"*3 + " SCENARIO 1: Customer enters and parks a car\n")
    car = Car("KA-01-HH-1234")
    print(f"→ Car {car.license_no} arrives at entrance")
    ticket1 = entrance.get_ticket(car)
    print("\n→ Updating display board after parking:")
    board.update(lot.get_all_spots())
    board.show_free_slot()

    # SCENARIO 2: CUSTOMER EXITS AND PAYS
    print("\n" + "▶"*3 + " SCENARIO 2: Customer exits and pays\n")
    print(f"→ Car {car.license_no} proceeds to exit panel")
    time.sleep(1.5)  # Simulate parking duration
    exit_panel.validate_ticket(ticket1)
    print("→ Updating display board after exit:")
    board.update(lot.get_all_spots())
    board.show_free_slot()

    # SCENARIO 3: FILLING LOT AND REJECTING ENTRY IF FULL
    print("\n" + "▶"*3 + " SCENARIO 3: Multiple customers attempt to enter\n")
    van = Van("KA-01-HH-9999")
    motorcycle = Motorcycle("KA-02-XX-3333")
    truck = Truck("KA-04-AA-9998")
    car2 = Car("DL-09-YY-1234")

    print(f"→ Van {van.license_no} arrives at entrance")
    ticket2 = entrance.get_ticket(van)
    
    print(f"\n→ Motorcycle {motorcycle.license_no} arrives at entrance")
    ticket3 = entrance.get_ticket(motorcycle)
    
    print(f"\n→ Truck {truck.license_no} arrives at entrance")
    ticket4 = entrance.get_ticket(truck)
    
    print(f"\n→ Car {car2.license_no} arrives at entrance")
    ticket5 = entrance.get_ticket(car2)

    print("\n→ Updating display board after several parkings:")
    board.update(lot.get_all_spots())
    board.show_free_slot()

    # Try to park another car (lot should be full)
    car3 = Car("UP-01-CC-1001")
    print(f"→ Car {car3.license_no} attempts to park (lot should be full):")
    ticket6 = entrance.get_ticket(car3)

    board.update(lot.get_all_spots())
    board.show_free_slot()

    print("\n" + "="*70)
    print("  END OF DEMONSTRATION".center(70))
    print("="*70 + "\n")

if __name__ == "__main__":
    main()