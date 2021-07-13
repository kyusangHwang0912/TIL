# 2번
keys = ['red','blue','yello','orange','black','white',
        'violet','pink','lime']
values = ['#ff0000','#0000ff','ffff00','ffa500','000000',
          'ffffff','ee82ee','ffc0cb','00ff00']
a = []
for i,j in zip(keys,values):
    a.append((i,j))
color_map = dict(a)

# 3번
color_name = input('칼라명을 영문으로 입력하세요 : ')

if color_name in color_map:
    print("{} 칼라의 RGB 값은 {}입니다".format(color_name,color_map[color_name]))
else:
    print("{} 칼라의 RGB 값을 찾을 수 없습니다.".format(color_name))

