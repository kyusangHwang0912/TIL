class Book :
    def __init__(self, title, author, price) :
        self.title = title
        self.author = author
        self.price = price

    def getBookinfo(self) :
        return str(self.title), str(self.author), str(self.price)

    def __str__(self) :
        return "Book 클래스로 생성된 객체"

book1 = Book("파이썬정복", "김상현", 22000)
print("[객체1 :", book1.__str__(),"]")
list1 = book1.getBookinfo()
print("책이름 : ", list1[0])
print("저자 : ", list1[1])
print("가격 : ", list1[2])
print()
book2 = Book("그립소", "유병로", 11700)
print("[객체2 :", str(book2),"]")
list2 = book2.getBookinfo()
print("책이름 : ", list2[0])
print("저자 : ", list2[1])
print("가격 : ", list2[2])
print()
book3 = Book("이것이 마이데이터다", "고은이", 13500)
print("[객체3 :", book3.__str__(),"]")
list3 = book3.getBookinfo()
print("책이름 : ", list3[0])
print("저자 : ", list3[1])
print("가격 : ", list3[2])
print()
book4 = Book("철학 100문장", "개러스 사우스웰", 11700)
print("[객체4 :", book4.__str__(),"]")
list4 = book4.getBookinfo()
print("책이름 : ", list4[0])
print("저자 : ", list4[1])
print("가격 : ", list4[2])
print()
book5 = Book("당신을 위한 육아나침반", "조영애", 14220)
print("[객체5 :", book5.__str__(),"]")
list5 = book5.getBookinfo()
print("책이름 : ", list5[0])
print("저자 : ", list5[1])
print("가격 : ", list5[2])

