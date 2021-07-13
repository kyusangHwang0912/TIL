def sumEven1(*args) :
    result = 0
    data_list = []
    data_list.append(args)
    for data in args:
        if data%2 == 0:
            result += data
    if data_list == [()]:
        result = -1
    return result

# 다양한 숫자
print(sumEven1(3,5))




