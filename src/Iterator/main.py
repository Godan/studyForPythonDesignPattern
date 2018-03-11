from BookShelf import BookShelf
from Book import Book
from Iterator import Iterator

def main():
    bookShelf = BookShelf()

    bookShelf.appendBook(Book("append"))
    bookShelf.appendBook(Book("GoF"))
    bookShelf.appendBook(Book("Design"))
    bookShelf.appendBook(Book("Pattern"))

    it = bookShelf.iterator()

    while(it.hasNext()):
        book = it.next()
        print(book.getName())


if __name__ == '__main__':
    main()
