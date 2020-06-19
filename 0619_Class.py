# 클래스

class Person:
    name = "길동"

    def say_hello(self):
        # 클래스 안에 선언된 변수를 사용할 때 self를 이용하여 사용
        print("Hello " + self.name)


# Person 이라는 객체의 오브젝트 생성
p = Person()

# Person 클래스의 함수 사용
p.say_hello()


# 함수 호출 시 인자값을 넘겨주는 법
# __init__ 을 사용
class Test:
    # 셀프를 먼저 선언하고, 사용할 값을 선언
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("Hello " + self.name + " , "+to_name)

    def introduce(self):
        print("이름 : " + self.name + ", " + " 나이 : " + str(self.age))


# 클래스 생성시 값 저장
wonie = Test("워니", 20)
michael = Test("마이클", 30)

# 함수 호출시 값 전달
wonie.say_hello("A")
michael.say_hello("B")

wonie.introduce()
michael.introduce()

# 1:07:31