a = [['B','C','A','A'],['C','C','B','B'],['D','A','A','D']]
a1 = 0
a2 = 0
a3 = 0
a4 = 0
for i in range(0,3) :
    for j in range(0,4):
        if a[i][j] == 'A':
            a1 += 1
        elif a[i][j] == 'B':
            a2 += 1
        elif a[i][j] == 'C':
            a3 += 1
        elif a[i][j] == 'D':
            a4 += 1
print('A 는 ',a1,'개 입니다.')
print('A 는 ',a2,'개 입니다.')
print('A 는 ',a3,'개 입니다.')
print('A 는 ',a4,'개 입니다.')