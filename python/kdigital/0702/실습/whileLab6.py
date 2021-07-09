while True:
    num = int(input('입력값 :'))
    if num==0:
        print('종료')
        break
    elif (num < -10) or (num > 10):
        continue
    elif num > 0:
        end_num = 2
        output = 1
        print('입력값 :',num)
        while end_num <= num:
            output *= end_num
            end_num += 1
        print(output)
    elif num < 0:
        num = -num
        print('입력값(부호변경) :',num)
        end_num = 2
        output = 1
        while end_num <= num:
            output = output * end_num
            end_num += 1
        print(output)