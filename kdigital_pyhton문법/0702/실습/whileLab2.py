import random
pairNum1 = random.randint(1,6)
pairNum2 = random.randint(1,6)

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    print(pairNum1,pairNum2)
    if pairNum1>pairNum2:
        print('pairNum1이 pairNum2보다 크다.')
    elif pairNum1<pairNum2:
        print('pairNum1이 pairNum2보다 작다.')
    else:
        print('게임끝')
        break