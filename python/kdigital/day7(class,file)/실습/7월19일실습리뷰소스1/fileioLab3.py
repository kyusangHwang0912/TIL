try:
    with open('yesterday.txt') as file:
        data = file.read()
        count = data.count("Yesterday") + data.count('yesterday')
except FileNotFoundError:
    print("파일을 읽을 수 없어요.")
else:
    print("Number of a word 'Yesterday'", count)
finally:
    print("수행완료!!")
