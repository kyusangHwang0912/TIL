listv = ["A", "b", "c", "D", "e", "F", "G", "h"]

listv2 = [x for x in listv if ord(x) >= 97]

print(listv2)