def print_triangle_withdeco(num,deco='%'):
    if (num<1) or (num>10):
        return
    else:
        for i in range(num):
            print(deco*(i+1))

print_triangle_withdeco(5,'*')

# 다양한 숫자
import random
for _ in range(5):
    num = random.randint(1,20)
    print(num)
    print_triangle_withdeco(num)
    print('-'*50)
