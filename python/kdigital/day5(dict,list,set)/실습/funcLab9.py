def sumEven1(*args):
    result = 0
    for data in args:
        if data%2 == 0:
            result += data

    if args == (): #len으로 확인하자..
        result = -1
    return result

# 다양한 숫자
print(sumEven1(2,3,4,5,6)) # 홀수 + 짝수
print(sumEven1(3,5)) # 홀수
print(sumEven1()) # 야규먼트 전달 x

###########################
def sumEven2(*nums):
    even_sum = 0
    if len(nums) >= 1:
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        return even_sum
    else:
        return -1

print(sumEven2(2,3,4,5,6)) # 홀수 + 짝수
print(sumEven2(3,5)) # 홀수
print(sumEven2()) # 야규먼트 전달 x




