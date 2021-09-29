import random
count = 0

while True:
    num = random.randint(0, 30)
    if (num>=1) and (num<=26):
        print('{}({})'.format(chr(num+64),num))
        count += 1
    elif (num==0) or (num>26):
        print('수행횟수는',count,'번입니다')
        break

# print(chr(num+64),"(",num,")",sep="") 으로도 가능!