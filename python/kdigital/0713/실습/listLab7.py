a = [[10,20,30,40,50],
     [5,10,15],
     [11,22,33,44],
     [9,8,7,6,5,4,3,2,13]
     ]

def raw_sum(x):
    sum = 0
    for i in range(len(a[x])):
        sum += a[x][i]
    return sum

for i in range(len(a)):
    print("{}행의 합은 {} 입니다.".format((i+1),raw_sum(i)))