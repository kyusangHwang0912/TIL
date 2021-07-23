col_dic = {'red': '#ff0000', 'blue': '#0000ff',
           'green': '#008000', 'yellow': '#ffff00',
           'orange': '#ffa500', 'black': '#000000',
           'white': '#ffffff', 'violet': '#ee82ee',
           'pink': '#ffc0cb', 'lime': '#00ff00'
           }

col = input("칼라명을 영문으로 입력하세요: ")
if col in col_dic:
    print(col, "칼라의 RGB 값은 ", col_dic[col], "입니다.", sep="")
else:
    print(col, "칼라의 RGB 값을 찾을 수 없습니다.", sep="")
