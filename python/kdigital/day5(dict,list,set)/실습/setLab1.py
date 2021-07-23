import random
a = set()
b = set()

for _ in range(10):
    a.add(random.randint(1,20))
    b.add(random.randint(1,20))

print('집합 1:',a)
print('집합 2:',b)
print('두 집합에 모두 있는 데이터', a & b)
print('집합1에는 있고 집합2에는 없는 데이터',a - b)
print('집합2에는 있고 집합1에는 없는 데이터',b - a)

union = a | b
intersection = a & b
print('집합1과 집합 2가 각자 가지고 있는 데이터',union.difference(intersection))