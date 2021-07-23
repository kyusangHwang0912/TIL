temper_dic = {'월': (26, 34), '화': (26, 33), '수': (26, 33), '목': (24, 33), '금': (24, 32), '토': (24, 33), '일': (25, 32)}

day = input("요일명을 한글로 입력하세요: ")
if day in temper_dic:
    print(day, "요일의 최저온도는 ", temper_dic[day][0], "이고 최고 온도는 ", temper_dic[day][1], "입니다.", sep="")
else:
    print(day, "요일의 정보를 찾을 수 없습니다.")
