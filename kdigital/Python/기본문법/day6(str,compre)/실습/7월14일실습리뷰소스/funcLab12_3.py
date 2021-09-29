def myprint(*num, **kargs):

  if 'deco' in kargs.keys() and 'sep' in kargs.keys():
    print(kargs['deco'], end='')
    for i in num:
        print(i, end=kargs['sep'])
        for keys, values in kargs.items():
            print(end='')
    print(kargs['deco'])

  elif 'deco' in kargs.keys() and 'sep' not in kargs.keys():
      print(kargs['deco'], end='')
      for i in num:
          print(i, end=',')
          for keys, values in kargs.items():
              print(end='')
      print(kargs['deco'])

  elif 'deco' not in kargs.keys() and len(num) != 0:
      print("**", end='')
      for i in num:
          print(i, end=',')
          for keys, values in kargs.items():
              print(end='')
      print("**")

  elif len(num) == 0 and len(kargs) == 0:
      print("Hello python")


myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco='$')
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()