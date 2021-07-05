while True:
    month = int(input('1~12월 사이의 값을 입력하세요 :'))
    if (month<1) or (month>12):
        print("1~12 사이의 값을 입력하세요!")
        break
    elif (month==12) or (month<3):
        print(month,'월은 겨울')
    elif (month>2) and (month<6):
        print(month,'월은 봄')
    elif (month>5) and (month<9):
        print(month, '월은 여름')
    else:
        print(month, '월은 가을')
