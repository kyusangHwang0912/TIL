def print_gugudan(x):
    if type(x) != int:
        return
    elif (x<1) or (x>9):
        return
    else:
        for i in range(1,10):
            print(x,"*",i,"=",x*i)

# 다양한 숫자
import random

for _ in range(5):
    x = random.randint(1,20)
    print("지금은",x,"단 입니다.")
    print_gugudan(x)
    print('-'*50)
