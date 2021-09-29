try:
    f = open("sample.txt", "rt", encoding="UTF-8")
    text = f.read()+"\n"
    f = open("sample_2021_07_19.txt", "at", encoding="UTF-8")
    f.write(text)
    print("저장이 완료되었습니다.")
except FileNotFoundError as e:
    print("파일이 없습니다. - ",e)

### datetime 함수랑 calendar 함수 이용해서 해결해보자.
