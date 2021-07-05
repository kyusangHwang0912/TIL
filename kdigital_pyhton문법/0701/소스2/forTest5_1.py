# 버전 2
startNum = int(input("시작 숫자 : "))
endNum = int(input("종료 숫자 : "))
incNum = int(input("증가치 숫자 : "))

if incNum == 0 :
    print("증가치는 0을 입력할 수 없으므로 기본값인 1로 처리함...")
    incNum = 1
for num in range(startNum, endNum-1, incNum) :
    print(num, end=" ")


