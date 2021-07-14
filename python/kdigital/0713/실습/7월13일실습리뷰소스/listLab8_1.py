lol = [['B', 'C', 'A', 'A'],
       ['C', 'C', 'B', 'B'],
       ['D', 'A', 'A', 'D']]

countA, countB, countC, countD = 0, 0, 0, 0
for i in range(3):
    for d in lol[i]:
        if d == 'A':
            countA += 1
        elif d == 'B':
            countB += 1
        elif d == 'C':
            countC += 1
        elif d == 'D':
            countD += 1

count = [countA, countB, countC, countD]

for i in range(4):
    print(chr(65+i), "는 ", count[i], "개 입니다.", sep="")