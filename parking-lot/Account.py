from enumerations import AccountStatus

class Account:
    def __init__(self, user_name=None, password=None, person=None, status=AccountStatus.ACTIVE):
        self.user_name = user_name
        self.password = password
        self.person = person
        self.status = status
    
    def reset_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            return True
        return False

class Admin(Account):
    def add_parking_spot(self, parking_lot, spot):
        parking_lot.add_spot(spot)
    
    def add_display_board(self, parking_lot, board):
        parking_lot.add_display_board(board)
    
    def add_entrance(self, parking_lot, entrance):
        parking_lot.add_entrance(entrance)
    
    def add_exit(self, parking_lot, exit_panel):
        parking_lot.add_exit(exit_panel)