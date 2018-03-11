from BookShelfIterator import BookShelfIterator

class BookShelf():

    def __init__(self):
        self._last = 0
        self._book = []

    def getBookAt(self, index: int):
        return self._book[index]

    def appendBook(self, book: object):
        self._book.append(book)
        self._last += 1

    def getLength(self):
        return len(self._book)

    def iterator(self):
        return BookShelfIterator(self)
