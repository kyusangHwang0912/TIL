listnum = [10, 5, 7, 21, 4, 8, 18]

result1 = listnum[0]
for i in listnum:
    if i < result1:
        result1 = i

result2 = listnum[0]
for i in listnum:
    if i > result2:
        result2 = i

print("최솟값 : {}, 최댓값 : {}".format(result1,result2))