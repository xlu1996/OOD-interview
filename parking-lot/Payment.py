from abc import ABC, abstractmethod
from datetime import datetime
from Payment import *
from enumerations import *

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
        self.status = PaymentStatus.PENDING
        self.timestamp = datetime.now()
    
    @abstractmethod
    def initiate_transaction(self):
        pass

class Cash(Payment):
    def initiate_transaction(self):
        self.status = PaymentStatus.COMPLETED
        return True

class CreditCard(Payment):
    def __init__(self, amount, card_number=None):
        super().__init__(amount)
        self.card_number = card_number
    
    def initiate_transaction(self):
        self.status = PaymentStatus.COMPLETED
        return True
