def main():
    class Taggable(object):
        def tag(self):
            pass

    class Book(Taggable):
        id = 0
        def __init__(self, author, title):
            if title == "":
                raise ValueError("incorrect title")
            self.title = title
            self.author = author

        def tag(self):
            self.tags = list()
            for w in self.title.split(' '):
                if w.istitle():
                    self.tags.append(w)
            return self.tags
        def __str__(self):
            return f"[{self.id}] {self.author} \'{self.title}\'"

    class Library:  
        def __init__(self, id, address):
            self.address = address
            self.id = id
            self.books  = list()
            self.itr = 0

        def __iadd__(self, book):
            book.id = len(self.books)+1
            self.books.append(book)
            return self

        def __iter__(self):
            return self

        def __next__(self):
            if self.itr < len(self.books):
                self.itr +=1
                return self.books[self.itr-1]
            raise StopIteration

    lib = Library(1, '51 Some str., NY')
    lib += Book('L.Tolstoi', 'War and Peace')
    lib += Book('Charles Dickens', 'David Copperfield')
    for book in lib:
        print(book)
        print(book.tag())
if __name__ == '__main__':
    main()