try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    text = f.read()
    text = text.lower()
    print("Number of a Word 'Yesterday' {}".format(text.count("yesterday")))
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    print("파일을 잘 읽어왔습니다.")
finally:
    print("수행완료!!")
