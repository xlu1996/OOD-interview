
## TODO - study this part
class DisplayBoard:
    def __init__(self, board_id):
        self.id = board_id
        self.parking_spots = {}
    
    def update(self, spots):
        self.parking_spots = {}
        for spot in spots:
            spot_type = spot.get_type()
            if spot_type not in self.parking_spots:
                self.parking_spots[spot_type] = []
            self.parking_spots[spot_type].append(spot)
    
    def show_free_slot(self):
        print(f"\n{'='*60}")
        print(f"  DISPLAY BOARD #{self.id} - AVAILABLE SPOTS".center(60))
        print(f"{'='*60}")
        
        if not self.parking_spots:
            print("  No parking spots registered".center(60))
            print(f"{'='*60}\n")
            return
        
        total_free = 0
        for spot_type, spots in sorted(self.parking_spots.items()):
            free_count = sum(1 for spot in spots if spot.is_free)
            total_count = len(spots)
            total_free += free_count
            
            status = "✓ Available" if free_count > 0 else "✗ FULL"
            print(f"  {spot_type:20} : {free_count}/{total_count} free   [{status}]")
        
        print(f"{'-'*60}")
        print(f"  TOTAL FREE SPOTS: {total_free}".center(60))
        print(f"{'='*60}\n")
