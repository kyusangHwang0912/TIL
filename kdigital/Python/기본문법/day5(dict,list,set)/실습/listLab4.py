import random
listnum = []
for _ in range(10):
    listnum.append(random.randint(1,50))
print(listnum) #4번
for i in range(len(listnum)):
    if listnum[i]<10:
        listnum[i] = 100

print(listnum) #6번
print(listnum[0]) #7
print(listnum[-1]) #8  #[len(listnum)-1]
print(listnum[1:6]) #9
print(listnum[::-1]) #10
print(listnum[:]) #11 #[::1]
del(listnum[4]) #12
print(listnum[:]) #13
del(listnum[1:3]) #14 #listnum[1:3] = []
print(listnum[:]) #15

print(listnum[-1::-1])
