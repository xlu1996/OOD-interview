class ParkingRate:
    def __init__(self):
        self.hourly_rate = 4.0
        self.additional_rate = 3.5
        self.extended_rate = 2.5
    
    def calculate(self, duration_hours, vehicle, spot):
        if duration_hours <= 0:
            return 0
        
        total = 0
        
        # First hour
        if duration_hours >= 1:
            total += self.hourly_rate
            duration_hours -= 1
        else:
            return round(self.hourly_rate * duration_hours, 2)
        
        # Hours 2-3
        if duration_hours >= 2:
            total += self.additional_rate * 2
            duration_hours -= 2
        elif duration_hours > 0:
            total += self.additional_rate * duration_hours
            return round(total, 2)
        
        # After 3 hours
        if duration_hours > 0:
            total += self.extended_rate * duration_hours
        
        return round(total, 2)