# 문자열 처리 함수

python = "Python is Amazing"

# 문자열을 전부 소문자로 출력
print(python.lower())

# 문자열을 전부 대문자로 출력
print(python.upper())

# 첫번째 문자가 대문자인지 확인해주는 명령어
# boolean으로 반환
print(python[0].isupper())

# 문자열을의 길이 반환
print(len(python))

# Python이라는 문자만 찾아서 다른 문자로 변경
print(python.replace("Python", "Java"))

# 문자열에서 n이 어디 있는지 확인
index = python.index("n")

print(index)

# 콤마를 찍고 뒤에꺼는 시작위치를 설정
# 이미 위에서 index가 5이기때문에 6번째부터 시작
index = python.index("n", index+1)

# 위의 index랑 동일하게 찾을 수 있음
print(python.find("n"))

# index랑 find의 다른점은
# index는 없는 문자일 경우 오류가 발생하여 에러 떨어짐
# find는 없는 문자일 경우 -1 라는 값을 반환함.


# 해당 문자안에 n이 몇번들어갔는지를 집계
print(python.count("n"))