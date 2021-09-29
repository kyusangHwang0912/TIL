import os
import calendar

path = "c:/iotest"
yoil = ['월', '화', '수', '목', '금', '토', '일']
birth_date = calendar.weekday(1999, 12, 4)
day = yoil[birth_date]

if not os.path.isdir(path) :
    os.mkdir(path)
os.chdir(path)

f = open("today.txt", "wt", encoding="UTF-8")
f.write(f"""오늘은 2021년 07월 19일입니다.
오늘은 월요일입니다.
나는 {day}요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")


