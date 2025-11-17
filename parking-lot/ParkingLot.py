
class ParkingLot:
    _instance = None
    _lock = Lock()
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("Use get_instance() instead")
        
        self.name = "Main Parking Lot"
        self.address = None
        self.parking_rate = ParkingRate()
        
        self.spots = []
        self.entrances = []
        self.exits = []
        self.display_boards = []
        self.active_tickets = []
        
        self.max_capacity = 40000
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    @staticmethod
    def reset_instance():
        """Reset singleton (for testing)"""
        ParkingLot._instance = None
    
    def add_spot(self, spot):
        self.spots.append(spot)
    
    def add_entrance(self, entrance):
        self.entrances.append(entrance)
    
    def add_exit(self, exit_panel):
        self.exits.append(exit_panel)
    
    def add_display_board(self, board):
        self.display_boards.append(board)
    
    def add_ticket(self, ticket):
        self.active_tickets.append(ticket)
    
    def remove_ticket(self, ticket):
        if ticket in self.active_tickets:
            self.active_tickets.remove(ticket)
    
    def get_all_spots(self):
        return self.spots
    
    def find_available_spot(self, vehicle):
        vehicle_type = vehicle.get_type()
        
        # Preferred spot types for each vehicle
        preferred_spots = {
            'Motorcycle': ['MotorcycleSpot', 'Compact'],
            'Car': ['Compact', 'Large', 'Handicapped'],
            'Van': ['Large'],
            'Truck': ['Large']
        }
        
        spot_preferences = preferred_spots.get(vehicle_type, ['Large'])
        
        for spot_type in spot_preferences:
            for spot in self.spots:
                if spot.get_type() == spot_type and spot.is_free:
                    return spot
        
        return None
    
    def find_spot_by_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                return spot
        return None
    
    def is_full(self):
        return all(not spot.is_free for spot in self.spots)
