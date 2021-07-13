def differtwovalue(x,y):
    if x>y:
        return x-y
    else:
        return y-x

# 1~30 난수 2개 추출 5회반복
import random
x = random.randint(1,30)
y = random.randint(1,30)

for _ in range(5):
    x = random.randint(1, 30)
    y = random.randint(1, 30)
    print(x,"와",y,"의 차는",differtwovalue(x,y),"입니다.")