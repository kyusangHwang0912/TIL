#1
import random
num = []
for _ in range(10):
    num.append(random.randint(1,100))

print(num)
#2
dict_num = {i+1:num for i,num in enumerate(num)}
check_pass = {num : 'pass' if value >= 60 else 'nopass' for num,value in dict_num.items()}
print(check_pass)
