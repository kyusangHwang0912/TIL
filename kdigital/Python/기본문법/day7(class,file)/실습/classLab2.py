class Book:
    books = []

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.books.append(self)

    def getBookInfo(self):
        return "{},{},{}".format(self.title, self.author, self.price)

    def __str__(self):
        self.result = "Book 클래스로 생성된 객체"
        return self.result

    @classmethod
    def print(cls):
        for i, book in enumerate(cls.books):
            print("[ 객체{}:{} ]".format(i + 1, str(book)))
            print(Book.getBookInfo(book).replace(',', '\n'))


Book("파이썬정복", "김상형", 22000)
Book("생활코딩", "이고잉", 27000)
Book("점프투장고", "박응용", 19800)
Book("마리아DB", "우재남", 30000)
Book("망고DB", "정승호", 28000)

Book.print()