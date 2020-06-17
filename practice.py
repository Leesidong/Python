# 출력 찍기
print(5)
print(-10)
print(3.14)
print(1000)
print(2*8)
print('풍선')
print("나비")
print("ㅋ"*9)
# #주석 처리
print(True)

print(not True)

# 변수형 타입
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 "+name+"이예요.")
# print(name+"는 "+str(age)+"이며, "+hobby+"을 아주 좋아해요.")
print(name, "는 ", age, "이며, ", hobby, "을 아주 좋아해요.")
print(name+"는 어른일까요? "+str(is_adult))

# 문자형을 제외한 정수형 및 불린형은 앞에 str() 로 붙여야 문자열에 사용이 가능함.
# 만약 안 쓸 경우 변수형에 , 찍어서 연결할 경우 그냥 사용이 가능함 또한 , 를 찍으면 띄워쓰기 하나씩 포함되어 있음.

# 주석이며

''' 이렇게 주석도 가능함
여러 라인을 주석하고 싶으면 단축키
ctrl + /
' < 이거 작은 따옴표임
으아 '''

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station+"행 열차가 들어오고 있습니다")

# 연산자
print(1+1)  # 2
print(3-2)  # 1
print(5-2)  # 3
print(6/3)  # 2

print(2**3)  # 2의 3승

print(5 % 3)  # 나머지 1
print(10 % 3)  # 1

print(5//3)  # 몫구하기
print(10//3)  # 3

print(10 > 3)  # True
print(4 >= 7)  # false
print(10 < 3)  # false
print(5 <= 5)  # true

print(3 == 3)  # true


print((3>0) and (3<5)) # true
print((3 > 0) & (3 < 5))  # true

print((3 > 0) or (5 < 3))  # true
print((3 > 0) | (5 < 3))

print(5>4>3) #true

print(5>4>7) #

## 33분
