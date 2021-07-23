s1 = "pythonjavascripy"
print(len(s1))

s2 = "010-7777-9999"
x, y, z = s2.split("-")
print(x, y, z, sep='')

s3 = "PYTHON"
print(s3[::-1])

s4 = "Python"
print(s4[0].lower(), s4[1:], sep='')

s5 = "https://www.python.org/"
print(s5.replace("/", ''))

s6 = '891022-2473837'
s6 = s6.split("-")
if s6[1].startswith("1") or s6[1].startswith("3"):
    print("남성입니다.")
if s6[1].startswith("2") or s6[1].startswith("4"):
    print("여성입니다.")

s7 = '100'
print(int(s7), float(s7))

s8 = 'The Zen of Python'
print(s8.count('n'))
print(s8.find('Z'))
print(s8.upper().split(' '))