import random
oper_num = random.randint(1,10)

if (oper_num==1) or (oper_num==6):
    result = 300 + 50
elif (oper_num==2) or (oper_num==7):
    result = 300 - 50
elif (oper_num==3) or (oper_num==8):
    result = 300 * 50
elif (oper_num==4) or (oper_num==9):
    result = 300 / 50
elif (oper_num==5) or (oper_num==10):
    result = 300 % 50
print(result)
