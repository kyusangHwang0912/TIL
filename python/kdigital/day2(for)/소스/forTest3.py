sum_value = 0
for num in range(1, 101):
    sum_value = sum_value +  num
print ("1부터 100까지 더한 값 =",sum_value)

sum_value = 0
for num in range(2, 101, 2):
    sum_value += num
print ("1부터 100까지 값들 중에서 짝수만 더한 값 =",sum_value)