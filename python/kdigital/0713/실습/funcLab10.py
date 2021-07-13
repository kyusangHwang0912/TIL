def sumAll(*args):
    result = 0
    for data in args:
        if type(data) == int and data != 0:
            result += data
        elif data == 0:
            result = "0 존재"
    if result == 0:
        result = None
    return result

print(sumAll(0,'a'))