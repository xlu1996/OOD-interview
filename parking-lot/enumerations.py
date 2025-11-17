from enum import Enum, auto

class PaymentStatus(Enum):
    COMPLETED = auto()
    FAILED = auto()
    PENDING = auto()
    REFUNDED = auto()

class AccountStatus(Enum):
    ACTIVE = auto()
    CLOSED = auto()
    CANCELED = auto()
    BLACKLISTED = auto()
    NONE = auto()

class TicketStatus(Enum):
    ISSUED = auto()
    IN_USE = auto()
    PAID = auto()
    VALIDATED = auto()
    CANCELED = auto()
    REFUNDED = auto()