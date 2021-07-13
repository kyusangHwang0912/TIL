import random
lotto_num = []

while True:
    num = random.randint(1,45)
    if num not in lotto_num:
        lotto_num.append(num)
    if len(lotto_num) == 6:
        break

print("행운의 로또번호 :",end=' ')
for i in range(len(lotto_num)-1):
    print(lotto_num[i],end=', ')
print(lotto_num[-1])