def myprint(*args, **kwargs):
    if 'deco' not in kwargs.keys():
        kwargs['deco'] = '**'
    if 'sep' not in kwargs.keys():
        kwargs['sep'] = ','
    lst = []
    if len(args) == 0:
        print('Hello Python')
    else:
        lst.append(kwargs['deco'])
        for i in args:
            lst.append(i)
            lst.append(kwargs['sep'])
        lst.append(kwargs['deco'])
        print(*lst[0:-2],lst[-1], sep='')


myprint(10, 20, 30, deco='@', sep='-')
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()