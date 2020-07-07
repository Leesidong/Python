print("hello world")

# 숫자형
print(5)

station ="사당"
print(station, "행 열차가 들어오고 있습니다")

station = "신도림"
print(station, "행 열차가 들어오고 있습니다")

station = "인천공항"
print(station, "행 열차가 들어오고 있습니다")

# 숫자 처리 함수
# 절대값
# abs

print(abs(-4))

# 승수
# pow

print(pow(4,2))

# 최대값
# max
print(max(5,12))

# 최소값
# min
print(min(4,1))

# 반올림
# round
print(round(3.14))
print(round(4.99))

# 랜덤 함수 사용법
# 파이썬에서 제공하는 random 라이브러리 사용

from random import *
print(random()) # 0.0 ~ 1.0 이하의 임의의 값 생성

print(random()*10) # 0.0 ~ 10.0 이하의 임의의 값 생성

print(int(random()*10)) # 0 ~ 10 이하의 임의의 값 생성

print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


# Quiz
print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4,28)) +"일로 선정되었습니다.")

