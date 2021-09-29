# version 3
# '구분자'.join(리스트) 함수를 이용 + map() 함수 이용해 Error 해결!!
def myprint(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        print("Hello Python")
    else:
        kwargs_dict = {"deco": "**", "sep": ","}    # default 값 생성
        kwargs_dict.update({k: v for k, v in kwargs.items()})   # kwargs 로부터 데이터 저장
        # print 를 한번만 사용해서 출력하기 위해 args 요소들 사이에 sep 넣은 lst 만들기 using "구분자".join(리스트)
        lst = list(args)
        # (int) 숫자가 포함된 경우 Error 발생 => map() 함수를 이용하여 list 내 숫자를 string 으로 변환!!
        str1 = kwargs_dict["sep"].join(map(str, lst))
        print(kwargs_dict["deco"], str1, kwargs_dict["deco"], sep="")   # deco 를 양 옆에 붙여서 *lst 출력


"""
# version 1 : join 함수를 사용하지 않고!!
def myprint(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        print("Hello Python")
    else:
        kwargs_dict = {"deco": "**", "sep": ","}    # default 값 생성
        kwargs_dict.update({k: v for k, v in kwargs.items()})   # kwargs 로부터 데이터 저장
        # print 를 한번만 사용해서 출력하기 위해 args 요소들 사이에 sep 넣은 lst 만들기
        lst = []
        for i in range(len(args)):
            if args[i] != args[-1]:     # 제일 마지막에는 sep 이 들어가면 안됨!
                lst.append(args[i])     # args 요소 하나 저장하고
                lst.append(kwargs_dict["sep"])  # sep 하나 저장
            else:                       # 제일 마지막 요소 뒤에는 아무것도 없이!
                lst.append(args[i])
        print(kwargs_dict["deco"], *lst, kwargs_dict["deco"], sep="")   # deco 를 양 옆에 붙여서 *lst 출력
"""

"""
# version 2
# '구분자'.join(리스트) 함수 사용? Error!!   숫자가 포함된 case 의 경우 Error
def myprint(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        print("Hello Python")
    else:
        kwargs_dict = {"deco": "**", "sep": ","}    # default 값 생성
        kwargs_dict.update({k: v for k, v in kwargs.items()})   # kwargs 로부터 데이터 저장
        # print 를 한번만 사용해서 출력하기 위해 args 요소들 사이에 sep 넣은 lst 만들기 using "구분자".join(리스트)
        lst = list(args)
        str1 = kwargs_dict["sep"].join(lst)

# Error
# Traceback (most recent call last):
#  File "C:/jha/PYTHONexam/day9/funcLab12.py", line 35, in <module>
#    myprint(10, 20, 30, deco="@", sep="-")
#  File "C:/jha/PYTHONexam/day9/funcLab12.py", line 30, in myprint
#    str1 = kwargs_dict["sep"].join(lst)
# TypeError: sequence item 0: expected str instance, int found

# => 원인: there are any non-string values in iterable, including bytes objects.

        print(kwargs_dict["deco"], str1, kwargs_dict["deco"], sep="")   # deco 를 양 옆에 붙여서 *lst 출력
"""

myprint()
myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
