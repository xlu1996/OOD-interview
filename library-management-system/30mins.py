from enum import Enum
from datetime import datetime, timedelta
from collections import defaultdict

# ============= ENUMS =============
class BookStatus(Enum):
    AVAILABLE = "available"
    LOANED = "loaned"
    RESERVED = "reserved"

class ReservationStatus(Enum):
    WAITING = "waiting"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# ============= CORE CLASSES =============
class BookItem:
    def __init__(self, barcode, title):
        self.barcode = barcode
        self.title = title
        self.status = BookStatus.AVAILABLE

class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name

class BookLending:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = datetime.now()
        self.due_date = datetime.now() + timedelta(days=14)
    
    def is_overdue(self):
        return datetime.now() > self.due_date

class BookReservation:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.status = ReservationStatus.WAITING
        self.created_date = datetime.now()

# ============= LIBRARY SYSTEM =============
class LibrarySystem:
    def __init__(self):
        self.lendings = {}  # barcode -> BookLending
        self.reservations = defaultdict(list)  # barcode -> [BookReservation]
    
    def checkout(self, member, book):
        if book.status != BookStatus.AVAILABLE:
            return False
        
        lending = BookLending(member, book)
        self.lendings[book.barcode] = lending
        book.status = BookStatus.LOANED
        return True
    
    def return_book(self, book):
        if book.barcode not in self.lendings:
            return False
        
        del self.lendings[book.barcode]
        book.status = BookStatus.AVAILABLE
        return True
    
    def reserve(self, member, book):
        if book.status == BookStatus.AVAILABLE:
            return False
        
        reservation = BookReservation(member, book)
        self.reservations[book.barcode].append(reservation)
        book.status = BookStatus.RESERVED
        return True
    
    def get_next_reservation(self, book):
        if book.barcode in self.reservations and self.reservations[book.barcode]:
            return self.reservations[book.barcode][0]
        return None
    
    def search(self, books, keyword):
        return [b for b in books if keyword.lower() in b.title.lower()]


# ============= DEMO =============
lib = LibrarySystem()

alice = Member("M001", "Alice")
bob = Member("M002", "Bob")
charlie = Member("M003", "Charlie")

book1 = BookItem("B001", "Design Patterns")
book2 = BookItem("B002", "Clean Code")
all_books = [book1, book2]

# Alice borrow book
print("Alice checkout:", lib.checkout(alice, book1))  # True

# Bob want to borrow same book -> failed
print("Bob checkout:", lib.checkout(bob, book1))  # False - already loaned

# Bob and charlie reserve
print("Bob reserve:", lib.reserve(bob, book1))  # True
print("Charlie reserve:", lib.reserve(charlie, book1))  # True

next_reservation = lib.get_next_reservation(book1)
print(f"Next in queue: {next_reservation.member.name}")  # Bob

# Alice return book
print("Alice return:", lib.return_book(book1))  # True

# search
print("Search 'Clean':", [b.title for b in lib.search(all_books, "Clean")])