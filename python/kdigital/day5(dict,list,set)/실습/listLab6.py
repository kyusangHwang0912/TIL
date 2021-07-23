a = [[10,12,13,16],
     [18,20,22,24],
     [26,28,30,32],
     [34,36,38,40]]
#1행 1열
print("1행 1열의 데이터 :",a[0][0])
#3행 4열
print("3행 4열의 데이터 :",a[2][3])
#행의 개수
print("행의 갯수 :",len(a))
#열의 개수
print("열의 갯수 :",len(a[1]))
#3행의 데이터들
print("3행의 데이터들 :",end=' ')
for i in range(len(a[2])):
    print(a[2][i],end=' ')
#2열의 데이터들
print()
print("2열의 데이터들 :",end=' ')
for i in range(len(a)):
    print(a[i][1],end=' ')
#왼쪽 대각선 데이터들
print()
print("왼쪽 대각선 데이터들 :",end=' ')
for i in range(len(a)):
    print(a[i][i],end=' ')
#오른쪽 대각선 데이터들
print()
print("오른쪽 대각선 데이터들 :",end=' ')
for i in range(len(a)):
    print(a[i][-i-1],end=' ')