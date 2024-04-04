from classes import Book, Case, Spot
from rfidreader import RfidReaderMock

# Make books
book1 = Book(1001, "Harry Potter 1")
book2 = Book(1002, "Harry Potter 2")
book3 = Book(1003, "Harry Potter 3")
# Make case 1
case1 = Case(1)
case1.allocate_book(1, 1, book1)
case1.allocate_book(1, 2, book2)
# Make case 2
case2 = Case(2)
case2.allocate_book(2, 1, book3)
# Make library consisting of two bookcases
library = [case1, case2]
# Make list for holding checked out books
books_checked_out = []

# Start testing
while True:
    print("Current situation in Library:\n")
    for case in library:
        print(case)
    print("Books checked out: ")
    i = 0
    for book in books_checked_out:
        print(f"{i}: {book}")
        i += 1
    
    command = input("Simulate RFID reader event: ")
    if command[0] == 'q':
        break
    cmd_parts = command.split(" ")
    case_nr = int(cmd_parts[1])
    case = library[case_nr - 1]
    shelf_nr = int(cmd_parts[2])
    spot_nr = int(cmd_parts[3])
    if cmd_parts[0] == "get":
        book = RfidReaderMock.simulate_book_taken_from_shelf(case, shelf_nr, spot_nr)
        if book is not None:
            books_checked_out.append(book)
    elif cmd_parts[0] == "put":
        book = books_checked_out[int(cmd_parts[4])]
        if book is not None:
            books_checked_out.remove(book)
            RfidReaderMock.simulate_book_put_on_shelf(case, shelf_nr, spot_nr, book)
    else:
        print("Illegal command")
