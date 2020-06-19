# 자료구조에는 리스트, 튜플, 딕셔너리 가 있음.

# 리스트
x = list()
y = []

# 두개가 같은 의미를 뜻함
# 파이썬의 리스트는 문자랑 숫자랑같이 사용 가능함
x = [1, 2, 3, "hello", "world"]
y = [4, 5, 7, "aa", "bb"]

print(x)
print(y)


# 리스트 2개를 하나롭 합칠 수도 있음.
print(x+y)

print(x[0])
print(x[4])

# 리스트 내용 바꾸기
# x 리스트의 0번째인 1을 10으로 바꿈
x[0] = 10
print(x[0])

# 리스트에서 쓰기 좋은 함수
x = [1,2,3,4]

num_length = len(x)

print(num_length)

# 정렬 
x = [4,3,2,1]

y = sorted(x)

print(y)

# 합계
z = sum(x)

print(z)

# 반복문 + 리스트

# x의 리스트 값을 하나씩 출력 시켜달라.
for n in x:
    print(n)

y = ["hello","there"]

for c in y:
    print(c)

# 리스트 안의 인자 값 인덱스 찾는 법
# x안에서 3이라는 값의 인덱스 찾기
x = [4,2,3,1]

print(x.index(3))
print(y.index("hello"))

# 리스트에 없는 값은 당연히 에러

# 인덱스 말고 있는지만 체크하고 싶을 경우
# True 또는 False 로 반환
print("hello" in y)

