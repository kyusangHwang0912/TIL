import random
start = random.randint(1,10)
end = random.randint(30,40)
sum = 0
for i in range(start,end+1):
    if i%2 == 0:
        sum += i

print(start,'부터',end,'까지의 짝수의 합:',sum)
