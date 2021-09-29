listnum = [10, 5, 7, 21, 4, 8, 18]

result = listnum[0]
for i in listnum:
    if i > result:
        result = i

print('최댓값:',result)