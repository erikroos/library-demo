class Book():
    def __init__(self, book_id, title):
        self.id = book_id
        self.title = title

    def __eq__(self, other):
        if other == None:
            return False
        return self.id == other.id
    
    def __str__(self):
        return str(self.id)

class Case():
    NR_OF_SHELVES = 3
    NR_OF_LOCATIONS_ON_SHELF = 4

    def __init__(self, case_id):
        self.id = case_id
        self.spots = []
        for i in range(Case.NR_OF_SHELVES):
            self.spots.append([])
            for _ in range(Case.NR_OF_LOCATIONS_ON_SHELF):
                self.spots[i].append(Spot())

    def allocate_book(self, shelf_nr, spot_nr, book):
        return self.spots[shelf_nr - 1][spot_nr - 1]._set_book(book)

    def get_book(self, shelf_nr, spot_nr):
        return self.spots[shelf_nr - 1][spot_nr - 1]._get_actual_book()
    
    def set_book(self, shelf_nr, spot_nr, book):
        return self.spots[shelf_nr - 1][spot_nr - 1]._set_actual_book(book)

    def __str__(self):
        retstr = f"               CASE{self.id}\n"
        retstr += "       1      2      3      4    \n"
        for i in range(Case.NR_OF_SHELVES):
            retstr += str(i + 1) + " [ "
            for j in range(Case.NR_OF_LOCATIONS_ON_SHELF):
                retstr += str(self.spots[i][j]) + " "
            retstr += "]\n"
        return retstr

class Spot():
    def __init__(self):
        self.book = None
        self.actual_book = None

    def _set_book(self, book):
        self.book = book
        self.actual_book = book

    def _get_actual_book(self):
        book_taken = self.actual_book
        self.actual_book = None
        return book_taken
    
    def _set_actual_book(self, book):
        if self.actual_book == None:
            self.actual_book = book
            return True
        return False
    
    def _is_spot_filled_correctly(self):
        return self.actual_book == self.book
    
    def __str__(self):
        if self.actual_book == None:
            # Empty spot
            if self.book == None:
                retstr = "|    |"
            else:
                retstr = "| XX |"
        else:
            # Book in spot
            if self._is_spot_filled_correctly():
                retstr = f"\033[92m|{self.actual_book}|\033[0m"
            else:
                retstr = f"\033[93m|{self.actual_book}|\033[0m"
        return retstr