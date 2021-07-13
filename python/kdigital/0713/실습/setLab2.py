import random
a = set()
while True:
    a.add(random.randint(1,45))
    if len(a) == 6:
        break

print('행운의 로또번호 :',end=' ')
a = list(a)
for i in range(len(a)-1):
    print(a[i],end=', ')
print(a[-1])
