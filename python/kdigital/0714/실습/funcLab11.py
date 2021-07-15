def mydict(**kargs):
    if len(kargs) == 0:
        return {}
    else:
        result = {'my '+ key:value for key,value in kargs.items()}
        return result

print(mydict(a=1,b=2,c=3,d=4))
print(mydict())
print(mydict(a='a',b='b'))









