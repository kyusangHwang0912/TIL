class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def getBookInfo(self):
        return f"{self.title},{self.author},{self.price}"

    def __str__(self) :
        return "Book 클래스로 생성된 객체"

b1 = Book("파이썬정복", "김상현", 22000)
b2 = Book("생활코딩! HTML+CSS+자바스크립트", "이고잉", 27000)
b3 = Book("돈을 부르는 작은 습관", "공형조", 15800)
b4 = Book("기억1", "베르나르 베르베르", 14800)
b5 = Book("적당히 가까운 사이", "댄싱스네일", 14500)

listd = [b1, b2, b3, b4, b5]
for num, data in enumerate(listd, 1):
    print("[객체 "+str(num)+" : "+str(data)+"]")
    print(data.getBookInfo().replace(",", "\n"))
    print("-" * 10)