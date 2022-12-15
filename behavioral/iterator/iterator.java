public interface Iterator {
    boolean hasNext();
    Object next();
}

public interface Aggregate {
    Iterator CreateIterator();
}

public class Book {
    private final String name;

    public Book(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

public class BookShelfIterator implements Iterator {
    private final BookShelfAggregate bookShelfAggregate;
    private int index;

    public BookShelfIterator(BookShelfAggregate bookShelfAggregate) {
        this.bookShelfAggregate = bookShelfAggregate;
        this.index = 0;
    }

    @Override
    public boolean hasNext() {
        return index < bookShelfAggregate.getLength();
    }

    @Override
    public Object next() {
        Book book = bookShelfAggregate.getBookAt(index);
        index++;
        return book;
    }
}

public class BookShelfAggregate implements Aggregate {
    private final Book[] books;
    private int last = 0;

    public BookShelfAggregate(int maxsize) {
        this.books = new Book[maxsize];
    }

    public Book getBookAt(int index) {
        return books[index];
    }

    public void appendBook(Book book) {
        this.books[last] = book;
        last++;
    }

    public int getLength() {

        return last;
    }

    @Override
    public Iterator CreateIterator() {
        return new BookShelfIterator(this);
    }
}

BookShelfAggregate bookShelfAggregate = new BookShelfAggregate(3);

bookShelfAggregate.appendBook(new Book("자바"));
bookShelfAggregate.appendBook(new Book("파이썬"));
bookShelfAggregate.appendBook(new Book("golang"));

System.out.println("개수 : "+bookShelfAggregate.getLength());

Iterator it = bookShelfAggregate.CreateIterator();

while(it.hasNext()){
    Book book = (Book) it.next();
    System.out.println(book.getName());
}

//개수 : 3
//자바
//파이썬
//golang
