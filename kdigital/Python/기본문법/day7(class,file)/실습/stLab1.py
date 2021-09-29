import calendar
while True:
    try:
        year_ = int(input('년도를 입력하세요 : '))
        month_ = int(input('월을 입력하세요 : '))
        calendar_= calendar.month(year_, month_)
        print(calendar_)
        break
    except ValueError:
        print("숫자가 입력되지 않았습니다.")

