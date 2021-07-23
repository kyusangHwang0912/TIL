import calendar
while True:
    y = input("해당 년도를 입력하세요 :")
    m = input("해당 월을 입력하세요 :")
    try:
        year = int(y)
        month = int(m)
        print(calendar.month(year, month))
        break
    except ValueError:
        print("입력 형식이 잘못되었습니다.")