def expr(num1,num2,calc):
    if calc == "+":
        return num1 + num2
    elif calc == "-":
        return num1 - num2
    elif calc == "*":
        return num1 * num2
    elif calc == "/":
        return num1 / num2

# 숫자 2개와 연산자 1개 사용자에게 받기
num1 = int(input('num1을 입력하시오 : '))
num2 = int(input('num2을 입력하시오 : '))
calc = input('+,-,*,/ 중 하나를 선택하시오 : ')

if expr(num1,num2,calc) == None:
    print("수행 불가")
else:
    print("연산결과 :",expr(num1,num2,calc))




