# 분기

# if

weater = "비"

# 기본 형식
if weater == "비":
    print("우산을 챙기세요.")

elif weater == "미세먼지":
    print("마스크를 챙기세요.")

else:
    print("준비물이 필요없어요.")

# 입력값 받는것
weater = input("오늘 날씨는 어때요? ")

# 기본 형식
if weater == "비" or weater == "눈":
    print("우산을 챙기세요.")

elif weater == "미세먼지":
    print("마스크를 챙기세요.")

else:
    print("준비물이 필요없어요.")

# 입력 값은 항상 문자로 받음
# 따라서 값을 정수로 쓰고 싶은 경우 정수로 바꿔줘야함.
temp = int(input("기온은 어때요?"))

if temp >= 30:
    print("너무 더워요. 나가지 마세요.")

elif temp <= 10 and temp < 30:
    print("괜찮은 날씨예요.")

elif 0 <= temp < 10:
    print("외투를 챙기세요.")

else:
    print("너무 추워요. 나가지 마세요.")


# 2:05:10
