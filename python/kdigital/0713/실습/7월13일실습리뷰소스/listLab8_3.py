# 1번
list_1 = [['B','C','A','A'],
          ['C','C','B','B'],
          ['D','A','A','D']
          ]

# 3번
A_sum = 0
B_sum = 0
C_sum = 0
D_sum = 0
for i in range(len(list_1)):
    A_sum += list_1[i].count('A')
    B_sum += list_1[i].count('B')
    C_sum += list_1[i].count('C')
    D_sum += list_1[i].count('D')
list_2 = [A_sum,B_sum,C_sum,D_sum]
print(list_2)

# 4번
chr = ['A','B','C','D']
for i in range(4):
    print('{} 는 {}개 입니다.'.format(chr[i],list_2[i]))