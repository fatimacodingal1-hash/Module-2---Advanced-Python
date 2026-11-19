# My Library Book Organiser (ACP starter, DSCM2L1). Python 3 standard library only.
# Run it in Google Colab (one cell) or as library_organiser.py. It runs now; do TODO 1 to TODO 4 in order.
# Lines marked (given) are done for you.

# (given) A: the books on the class library shelf today.
books = ["Matilda", "The Jungle Book", "Charlotte's Web", "Holes"]

# TODO 1: add "Wonder" to the end of books, then remove
#   "The Jungle Book" only if it is in the list, then sort books from A to Z.
#   Check: "Books: 4 ["Charlotte's Web", 'Holes', 'Matilda', 'Wonder']".
print("Books:", len(books), books)
print("First:", books[0], "| Last:", books[-1])               # (given) B

# (given) C: the shelf code of each book, in the same order as the sorted list.
shelves = ["C1", "H2", "M1", "W3"]

# TODO 2: make a dictionary called shelf_of that maps each
#   book to the shelf code at the same position (use zip, then dict).
#   Check: "Shelf map: {"Charlotte's Web": 'C1', 'Holes': 'H2', 'Matilda': 'M1', 'Wonder': 'W3'}".
shelf_of = {}  # (given) placeholder: replace this line
print("Shelf map:", shelf_of)


def where_is(book):
    """Return the shelf code, or a message if the library does not have the book."""
    # TODO 3: return the shelf code for book, or
    #   "Not in this library" when the book is not a key (use get with a default).
    #   Check: "Holes -> H2" and "Dune -> Not in this library".
    return "?"  # (given) placeholder: replace this line


for title in ["Holes", "Dune"]:                                # (given) D
    print(title, "->", where_is(title))

librarian = {"name": "Ms. Paula", "desk": "Front"}             # (given) E
# TODO 4: change "desk" to "Reading Room", add the key
#   "books_today" with the number of books (use len), then print librarian.
#   Check: "Librarian: {'name': 'Ms. Paula', 'desk': 'Reading Room', 'books_today': 4}".
