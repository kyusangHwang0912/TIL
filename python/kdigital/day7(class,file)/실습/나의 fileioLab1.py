
import os
os.chdir("C:\\")
if os.path.exists("iotest"):
    os.chdir("C:\\iotest")
else:
    os.mkdir("iotest")
    os.chdir("C:\\iotest")

try:
    f = open("today.txt", "rt", encoding="UTF-8")
    text = f.read()
    print(text)
except FileNotFoundError as e:
    print("파일이 없습니다. - ",e)
    print("따라서 파일을 새로 생성하겠습니다.")
    f = open("today.txt", "wt", encoding="UTF-8")
    f.write("""오늘은 2021년 07월 19일입니다.
오늘은 월요일입니다.
나는 수요일에 태어났습니다.""")
    f = open("today.txt", "rt", encoding="UTF-8")
    text = f.read()
    print(text)
    print("저장이 완료되었습니다.")