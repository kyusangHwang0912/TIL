keys = ['월','화','수','목','금','토','일']
values = [(33,25),(33,25),(33,24),(32,23),(33,24),(31,24),(33,25)]

a = []
for i,j in zip(keys,values):
    a.append((i,j))
weather = dict(a)


week = input('요일명을 한글로 입력하세요 :')

if week in weather:
    print("{}요일의 최저온도는 {} 이고 최고 온도는 {}입니다".format(week,weather[week][0],weather[week][1]))
else:
    print("{}요일의 정보를 찾을 수 없습니다.".format(week))