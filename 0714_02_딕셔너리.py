# 딕셔너리

# 키에 대한 중복은 안됨

# 기본 형식
cabinet = {3: "유재석", 100 : "김태호"}

# 키 값을 넣어주면됨
print(cabinet[3])
print(cabinet[100])

# 위와 동일한 형식
print(cabinet.get(3))

# 1번 형식으로 
# 만약 없을 경우
# print(cabinet[5])
# 오류처리 됨.


# 2번 형식으로
# 만약 없을 경우
# print(cabinet.get(5))
# null 로 값이 반환됨
# 오류 처리 안됨

# 만약 null이 아닌 다른 값으로 반환을 원할 경우
# print(cabinet.get(5), "여기에 넣음")

# 딕셔너리 안에 값이 있는지 확인
# true / false로 반환
# 앞에는 키값을 넣어야함.
print( 3 in cabinet)


# 키 값은 정수형이 아닌 문자로도 가능함
cabinet = { "A-3":"유재석", "A-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["A-100"])

# 신규 값 추가
print(cabinet)

cabinet["C-20"] = "조세호"

print(cabinet)

cabinet["A-3"] = "김종국"
print(cabinet)

# 값 제거
del cabinet["A-3"]

print(cabinet)

# 키들만 출력
print(cabinet.keys())

# 값들만 출력
print(cabinet.values())

# 키와 값을 출력
print(cabinet.items())

# 딕셔너리 초기화
cabinet.clear()
print(cabinet)