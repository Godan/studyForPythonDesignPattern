import Iterator
import BookShelf

class BookShelfIterator(Iterator):

    def __init__(self, BookShelf):
        self._bookShelf = BookShelf
        self.index = 0

    def hasNext(self):
        print (self.index)
        print (self._bookShelf.getLength())
        if(self.index < self._bookShelf.getLength()):
            return True
        else:
            return False

    def next(self):
        book = self._bookShelf.getBookAt(self.index)
        self.index += 1
        return book
