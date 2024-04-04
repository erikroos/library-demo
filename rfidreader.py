class RfidReaderMock():
    def simulate_book_taken_from_shelf(case, shelf_nr, spot_nr):
        return case.get_book(shelf_nr, spot_nr)
    
    def simulate_book_put_on_shelf(case, shelf_nr, spot_nr, book):
        return case.set_book(shelf_nr, spot_nr, book)