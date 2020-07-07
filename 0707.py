# 상속

class Person:
    def __inif__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! "+ to_name +" 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

# 클래스를 만들때 소괄호를 써서 안에 상속할 클래스를 입력하면 클래스가 상속됨
class Police(Person):
    def arrest(self, to_arrest):
        print("넌 채포됐다, "+to_arrest)


class Programer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다!"+to_program)


wonie = Person("워니", 20)

jenney = Police("제니",21)

michael = Programer("마이클",21)

wonie.introduce()

# 제니와 마이클 객체의 클래스에는 introduce가 없음. 하지만 Person을 상속받았기 때문에 Person에 있는 함수를 쓸 수 있음.
jenney.introduce()

michael.introduce() 

#jenney.arrest("워니")

#michael.program("이메일 클라이언트")