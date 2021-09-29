from random import randint


num_set1, num_set2 = set(), set()
while len(num_set1) < 10:
    num_set1.add(randint(1, 20))
while len(num_set2) < 10:
    num_set2.add(randint(1, 20))
print("집합1 :", num_set1)
print("집합2 :", num_set2)
print("두 집합에 모두 있는 데이터 :", num_set1 & num_set2)
print("집합1 또는 집합2 에 있는 데이터 :", num_set1 | num_set2)
print("집합1에는 있고 집합2에는 없는 데이터 :", num_set1 - num_set2)
print("집합2에는 있고 집합1에는 없는 데이터 :", num_set2 - num_set1)
print("집합1과 집합 2가 각자 가지고 있는 데이터 :", num_set1 ^ num_set2)
