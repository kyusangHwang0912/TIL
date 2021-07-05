print("3 + 4 = ?")
while True:
    a = input("정답을 입력하시오 : ")
    if len(a) == 0:
        print("공백입니다. 숫자를 입력하세요")
    elif a == '7':
        break
    elif a != '7':
        print('틀렸습니다.')


print("참 잘했어요")