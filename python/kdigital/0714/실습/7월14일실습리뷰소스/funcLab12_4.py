def myprint(*str_tuple, **str_dict):
    if len(str_tuple) == 0:
        print("Hello Python")
        return
    str_list = [n for n in str_tuple]
    str_list[0] = str_dict.get("deco", '**') + str(str_list[0])
    str_list[-1] = str(str_list[-1]) + str_dict.get("deco", '**')
    print(*str_list, sep=str_dict.get("sep", ','))


myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()
