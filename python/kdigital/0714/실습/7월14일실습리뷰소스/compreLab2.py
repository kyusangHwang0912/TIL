def mycompredict(**kargs):

    mykargs = { "my"+k : v for k, v in kargs.items()}

    return mykargs


print(mycompredict(a=2, b=3))
print(mycompredict(a=2))
print(mycompredict())