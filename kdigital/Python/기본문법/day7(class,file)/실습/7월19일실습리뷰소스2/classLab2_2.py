class Book:
    """
    책의 이름, 작가, 가격에 대한 정보를 저장합니다.
    getBookInfo
    """
    # 책의 이름, 작가, 가격을 초기화합니다.
    def __init__(self, tilte, author, price):
        self.tilte = str(tilte)
        self.author = str(author)
        self.price = int(price)

    # Book 인스턴스가 가진 정보를 문자열로 반환합니다.
    def getBookInfo(self):
        return f"{self.tilte}\n{self.author}\n{self.price}"

    # "Book 클래스로 생성된 객체"를 반환합니다.
    def __str__(self):
        return "Book 클래스로 생성된 객체"


# 5개의 Book 인스턴스를 생성합니다.
book1 = Book("파이썬 정복", "김상형", 22000)
book2 = Book("koob1", "moon", 80000)
book3 = Book("koob2", "moon", 70000)
book4 = Book("koob3", "moon", 60000)
book5 = Book("koob4", "moon", 50000)
# book 인스턴스들을 리스트로 만듭니다.
book_list = [book1, book2, book3, book4, book5]
# 각각의 인스턴스들의 정보를 형식에 맞게 출력합니다.
for no, book in enumerate(book_list, 1):
    print(f"[ 객체{no} : {str(book)} ]")
    print(book.getBookInfo())
