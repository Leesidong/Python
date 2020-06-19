# 딕셔너리

# 동일하게 2가지 방식이 있음

x = dict()
y = {}

print(x)
print(y)

# 앞의 2가지와 다른 점은 앞의 용어를 쓰느냐에 따라 괄호가 틀림
# 안쓸 경우는 중괄호
# 대괄호 : 리스트, 중괄호 : 딕셔너리, 소괄호 : 튜플

# 앞의 두 가지와 다른 점은 키와 값으로 이루어져 있음

# 키 값에는 불변하는 값만 사용이 가능함
# 문자열이나 숫자
x = {
    "name": "워니",
    "age": 20,
}

print(x)
print(x["name"])
print(x["age"])

#방식이 C#의 DataRow에서 값 사용할 때랑 비슷함.

x = {
    0: "Wonie",
    1: "Hello",
    "age": 20,
}

print(x[0])
print(x[1])
print(x["age"])

# 키 값을 확인

print("age" in x)

print("name" in x)

# 딕셔너리에서 유용한 함수

# 딕셔너리에 들어있는 키를 보여줌
print(x.keys())

# 딕셔너리에 들어있는 값을 보여줌
print(x.values())

# 반복문 + 딕셔너리
for key in x:
    print("key : " + str(key))
    print("value :" + str(x[key]))


# 딕셔너리도 리스트와 동일하게 값을 변경할 수 있음.
x[0] = "길동"
print(x)

# 새로운 값에 키 값을 넣기
x["school"] = "한빛"

print(x)