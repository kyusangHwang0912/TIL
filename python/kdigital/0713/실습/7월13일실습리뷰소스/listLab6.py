lst = [
    [10, 12, 14, 16],
    [18, 20, 22, 24],
    [26, 28, 30, 32],
    [34, 36, 38, 40]
]

# 1
print("1행 1열의 데이터 : ", lst[0][0])
# 2
print("3행 4열의 데이터 : ", lst[2][3])
# 3
print("행의 갯수 : ", len(lst))
# 4
print("열의 갯수 : ", len(lst[0]))
# 5
print("3행의 데이터들 : ", end="")
for i in lst[2]:
    print(i, end=" ")
print()
# 6
print("2열의 데이터들 : ", end="")
for i in range(len(lst)):
    print(lst[i][1], end=" ")
print()
# 7
print("왼쪽 대각선 데이터들 : ", end="")
for i in range(len(lst)):
    print(lst[i][i], end=" ")
print()
# 8
print("오른쪽 대각선 데이터들 : ", end="")
for i in range(len(lst)):
    print(lst[i][len(lst) - 1 - i], end=" ")
print()
