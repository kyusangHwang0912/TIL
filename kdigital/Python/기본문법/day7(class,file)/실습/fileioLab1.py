
##### date와 calendar 사용해서 하드코딩하지 말고 구현해보자.

import os
import datetime

now = datetime.datetime.now()
mybirthday = datetime.date(1995,9,12)
week = now.weekday()
mybirthday_week = mybirthday.weekday()
yoil = ['월','화','수','목','금','토','일']

if not os.path.isdir("C:/iotest"):
    os.mkdir("C:/iotest")
    f = open("C:/iotest/today.txt","wt",encoding="UTF-8")
    f.write("""오늘은 {}년 {}월 {}일입니다.
오늘은 {}요일입니다.
나는 {}요일에 태어났습니다.""".format(now.year,now.month,now.day,yoil[week],yoil[mybirthday_week]))
    f = open("C:/iotest/today.txt","rt",encoding="UTF-8")
    text = f.read()
    print(text)

