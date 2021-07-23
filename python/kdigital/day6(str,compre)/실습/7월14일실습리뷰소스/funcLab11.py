def mydict(**kargs):
    mykargs = {}
    for k, v in kargs.items():
        mykargs["my"+k] = v
    return mykargs


print(mydict(a=2, b=3))
print(mydict(a=2))
print(mydict())


