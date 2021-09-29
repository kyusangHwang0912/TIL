lst = [
    [10, 20, 30, 40, 50],
    [5, 10, 15],
    [11, 22, 33, 44],
    [9, 8, 7, 6, 5, 4, 3, 2, 13]
]


for row in range(len(lst)):
    row_sum = 0
    for col in lst[row]:
        row_sum += col
    print(row + 1, "행의 합은 ", row_sum, "입니다.", sep="")