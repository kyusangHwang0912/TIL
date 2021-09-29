def myprint (*p, deco="**",sep=",") :
    if p is None :
        print("Hello Python")
    else :
        print(deco, end="")
        print(*p, sep=sep, end="")
        print(deco)

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
