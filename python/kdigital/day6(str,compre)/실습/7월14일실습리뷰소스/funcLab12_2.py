def myprint(*args, **kwargs):
    if not args and not kwargs:
        print("Hello Python")
        return

    init_kw = {"deco": "**", "sep": ","}
    init_kw.update(kwargs)

    args_sep = []
    for i in args:
        args_sep.append(str(i))
        args_sep.append(init_kw["sep"])
    args_sep = ''.join(args_sep[:-1])

    print(init_kw["deco"], args_sep, init_kw["deco"], sep="")


myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
