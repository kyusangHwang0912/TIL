import os
import calendar
import datetime

now = datetime.datetime.now()
yoil = ['월', '화', '수', '목', '금', '토', '일']
day = calendar.weekday(1997,9,3)

if not os.path.isdir("c:/iotest"): # 존재하는가?
    os.mkdir("c:/iotest") # 없으면 만들어줘.

f = open("c:/iotest/today.txt", "wt", encoding="UTF-8")
f.write(f"""오늘은 {now.year}년 {now.month:02d}월 {now.day:02d}일입니다.
오늘은 {yoil[calendar.weekday(now.year,now.month,now.day)]}요일입니다.
나는 {yoil[day]} 요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")


