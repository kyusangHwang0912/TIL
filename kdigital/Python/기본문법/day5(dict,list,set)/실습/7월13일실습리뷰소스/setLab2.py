import random

s = set() # {v1, v2, ... }, {}
while len(s) < 6:
    s.add(random.randint(1, 45))

print("행운의 로또번호 : ", end="")
for d in s:
    print(d, end=" ")
print()

print('행운의 로또번호 :',end=' ')
a = list(s)
for i in range(len(a)-1):
    print(a[i],end=',')
print(a[-1])