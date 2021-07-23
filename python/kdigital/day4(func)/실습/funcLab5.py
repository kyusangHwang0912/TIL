def print_triangle(x):
    if (x>=1) and (x<=10):
        for i in range(x,0,-1):
            print('@'* (i))

# 다양한 숫자
import random
for _ in range(5):
    x = random.randint(1,20)
    print("아규먼트 값 = ",x)
    print_triangle(x)
    print('-' * 50)