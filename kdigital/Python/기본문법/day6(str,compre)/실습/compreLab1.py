def createList(*args,type=1):
    if type == 2:
        result = [data for data in args if not data%2]
    elif type == 3:
        result = [data for data in args if data%2]
    elif type == 4:
        result = [data for data in args if data>10]
    elif type == 1:
        result = [data for data in args]
    if len(args) == 0:
        a= []
        for i in range(30):
            a.append(i+1)
        result = createList(*a[:],type=type)
    return result

def createList(*args,type=1):
    if len(args) == 0:
        args = [data for data in range(1,31)]

    if type == 2: #elif하면 안됨..
        result = [data for data in args if not data%2]
    elif type == 3:
        result = [data for data in args if data%2]
    elif type == 4:
        result = [data for data in args if data>10]
    elif type == 1:
        result = [data for data in args]
    else:
        result = []
    return result

print(createList())
print(createList(type=1))
print(createList(type=2))
print(createList(type=3))
print(createList(type=4))
print(createList(1,2,3,4,5,6,2,type=2))
