import datetime, os

if not os.path.exists("C:/iotest"):
    os.makedirs("C:/iotest")
f = open("c:/iotest/today.txt", "wt", encoding="UTF-8")
days = ['월', '화', '수', '목', '금', '토', '일']
f.write(f"""오늘은 2021년 07월 19일입니다.
오늘은 월요일입니다.
나는 {days[datetime.date(1993, 4, 28).weekday()]}요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")
