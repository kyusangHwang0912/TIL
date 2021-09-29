while True:
    word = input('문자열을 입력하시오 :')
    wordlengh = len(word)
    if wordlengh == 0:
        break
    elif (wordlengh>=5) and (wordlengh<=8):
        continue
    elif wordlengh<5:
        result = '*'+word+'*'
        print('유효한 입력 결과 :',result)
    else:
        result = '$'+word+'$'
        print('유효한 입력 결과 :', result)

