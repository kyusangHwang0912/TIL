import random

lst = [] # list()
while len(lst) < 6:
    num = random.randint(1, 45)
    if num not in lst:
        lst.append(num)


print("행운의 로또번호 : ", end="")
for num in lst:
    print(num, end=" ")
print()

print('행운의 로또번호 :',end=' ')
for i in range(len(lst)-1):
    print(lst[i],end=',')
print(lst[-1])