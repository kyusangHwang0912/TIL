lst = [
    ['B', 'C', 'A', 'A'],
    ['C', 'C', 'B', 'B'],
    ['D', 'A', 'A', 'D']
]


data = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
count_lst = []
for d in data.values(): # for _, d in data.items() :
    count = 0
    for row in lst:
        count += row.count(d)
    count_lst.append(count)

for i, d in data.items():
    print(d, "는 ", count_lst[i], "개 입니다.", sep="")
