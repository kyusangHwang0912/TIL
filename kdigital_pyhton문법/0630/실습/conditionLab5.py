import random
score = random.randint(0,100)

if (score>=90) and (score<=100):
    print(score,'점은 A등급입니다.')
elif (score>=80) and (score<=89):
    print(score,'점은 B등급입니다.')
elif (score>=70) and (score<=79):
    print(score,'점은 C등급입니다.')
elif (score>=60) and (score<=69):
    print(score,'점은 D등급입니다.')
else:
    print(score,'점은 F등급입니다.')