def mycompredict(**kargs):
    if len(kargs) == 0:
        return {}
    else:
        result = {'my '+ key:value for key,value in kargs.items()}
        return result

print(mycompredict(a=1,b=2,c=3,d=4))
print(mycompredict())
print(mycompredict(a='a',b='b'))