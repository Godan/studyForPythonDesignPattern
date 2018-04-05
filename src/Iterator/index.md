# Pythonで学ぶ「デザインパターン入門」

## Iterator Pattern
イテレーターパターンはある集合体から一つづつ取り出し処理を行うパターンです。例えば、本棚であれば一冊づつ本を取り出して本ごとに処理を行うようなものです。

### 出て来る概念たち
今回は書籍の方でも紹介されている本棚の例を参考にしていきます。


#### Aggregat（集合体クラス）
数え上げるものの「集合体」を扱います。今回の例では本棚（書籍の集合体）が該当します。機能としては

* getBookAt() … 指定された要素を返す
* appendBook() … 要素を最後に追加する
* getLength() … 配列の長さを返す
* iterator() … イテレーターを返す

を実装しています。


``` Python
from BookShelfIterator import BookShelfIterator

class BookShelf():

    def __init__(self):
        self._last = 0
        self._book = []

    # 指定された要素を返す
    def getBookAt(self, index: int):
        return self._book[index]

    # 本を配列の最後に追加する
    def appendBook(self, book: object):
        self._book.append(book)
        self._last += 1

    # 配列の長さを取得する
    def getLength(self):
        return len(self._book)

    # イテレーターを返す
    def iterator(self):
        return BookShelfIterator(self)

```

#### iterator (反復子クラス)
イテレータークラスは実際に集合体を走査し、ひとつづつ数え上げるクラスです。本棚から一つづつ本を取り出すインターフェースを定義実装しています。  
主に

* hasNext() … 集合体に次の要素があるのか
* next() … 次の要素をとりだす

の2つを実装しています。
```Python
import Iterator
import BookShelf

class BookShelfIterator(Iterator):

    def __init__(self, BookShelf):
        self._bookShelf = BookShelf
        self.index = 0

    def hasNext(self):
        if(self.index < self._bookShelf.getLength()):
            return True
        else:
            return False

    def next(self):
        book = self._bookShelf.getBookAt(self.index)
        self.index += 1
        return book

```

#### UML
[![](http://www.plantuml.com/plantuml/svg/RL112i903Bpd5NjKP7yWKhq9qeilI6riYsrIkX4Buj_DTYiMz9JCP38JaWN5GUzT2m2N5aDm1v6RUu9pdh4ZgvkADBTsjORNKdIkgRqcfN4QQs7ql14LUxKTWzZtn6La3AVnYRZIEi56QK2LuM_0SHvEEQxuq1DgkAGnEjGOSXhdDBOkMNsl5B-RB1VKrfVoO2-_KG2GsRtnAMy0)](http://www.plantuml.com/plantuml/uml/RL112i903Bpd5NjKP7yWKhq9qeilI6riYsrIkX4Buj_DTYiMz9JCP38JaWN5GUzT2m2N5aDm1v6RUu9pdh4ZgvkADBTsjORNKdIkgRqcfN4QQs7ql14LUxKTWzZtn6La3AVnYRZIEi56QK2LuM_0SHvEEQxuq1DgkAGnEjGOSXhdDBOkMNsl5B-RB1VKrfVoO2-_KG2GsRtnAMy0)

### 実際に使うプログラム

```python
from BookShelf import BookShelf
from Book import Book
from Iterator import Iterator

def main():
    bookShelf = BookShelf()

    # 本を追加する
    bookShelf.appendBook(Book("ステラのまほう"))
    bookShelf.appendBook(Book("東京トイボックス"))
    bookShelf.appendBook(Book("ゆるきゃん▲"))
    bookShelf.appendBook(Book("僕達のリメイク"))
    bookShelf.appendBook(Book("りゅうおうのおしごと！"))

    it = bookShelf.iterator()

    # 本を取り出し名前を出力する
    while(it.hasNext()):
        book = it.next()
        print(book.getName())


if __name__ == '__main__':
    main()

```


## 何が嬉しいのか
### どのような実装であれ用いれる
列挙していく処理はイテレーターに実装されているためもし集合体クラスに何か変更があってもWile文には影響されない。
