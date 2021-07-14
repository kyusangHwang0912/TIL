import random

s1 = set()
s2 = set()

for _ in range(10):
    s1.add(random.randint(1, 20))
    s2.add(random.randint(1, 20))

# 1
print("집합1: ", s1)
print("집합2: ", s2)
# 2 : 교집합
print("두 집합에 모두 있는 데이터: ", s1 & s2)
# 3 : 합집합
print("집합1 또는 집합2에 있는 데이터: ", s1 | s2)
# 4 : 차집합
print("집합1에는 있고 집합2에는 없는 데이터: ", s1 - s2)
print("집합2에는 있고 집합1에는 없는 데이터: ", s2 - s1)
# 5 : 대칭차집합
print("집합1과 집합2가 각자 가지고 있는 데이터: ", s1 ^ s2)
