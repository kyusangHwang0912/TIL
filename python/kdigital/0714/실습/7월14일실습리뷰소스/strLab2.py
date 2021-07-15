s1 = 'pythonjavascript'
print(len(s1))

s2 = "010-7777-9999"
print(s2.replace("-", ""))

s3 = "PYTHON"
print(s3[::-1])

s4 = "Python"
print(s4.lower())

s5 = "http://www.python.org/"
print(s5.lstrip('"').rstrip('"').rstrip('/'))

s6 = '891022-2473837'

s6_1 = s6.split("-")

s6_2 = s6_1[1]

if s6_2[0] == '1' or s6_2[0] == '3':
    s6_sex = '남성'
elif s6_2[0] == '2' or s6_2[0] == '4':
    s6_sex = '여성'

print(s6_sex)

s7 = '100'
print(int(s7))
print(float(100))

s8 = 'The Zen of Python'
print(s8.count('n'))

print(s8.find('Z'))

s9 = s8.upper()

print(s9.split(" "))







