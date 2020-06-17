#퀴즈1
#함수로 만들기

# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"이라고 말하라
# 나이가 10살에서 20살 사이면 "안녕하세요"라고 말해라
# 그 외에는 "안녕하십니까" 라고 말해라

def quiz(name, age):
    print("나 : "+name)
    if age < 10:
        print("안녕")
    elif age >= 10 and age <=20:
        print("안녕하세요")
    else:
        print("안녕하십니까")


quiz("길동", 10)