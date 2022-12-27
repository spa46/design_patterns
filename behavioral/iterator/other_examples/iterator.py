class Book:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class BookShelf:
    def __init__(self):
        self._book = []
        self._last = 0
        self._current = 0

    def append(self, book):
        self._book.append(book)
        self._last += 1

    def length(self):
        return self._last

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._last:
            r = self._current
            self._current += 1
            return self._book[r]
        else:
            raise StopIteration

    def has_next(self):
        return self._current < self._last

book_shelf_iterator = BookShelf()

book_shelf_iterator.append(Book('java'))
book_shelf_iterator.append(Book('python'))
book_shelf_iterator.append(Book('golang'))

print('num: ', book_shelf_iterator.length())

for book in book_shelf_iterator:
    print(book.name)
