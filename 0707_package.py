# animal Package
# dog, cat Modual 생성
# dog, cat Modual Can Say "Hi"

# Package 구성시 폴더를 생성해야 Package가 됨 폴더의 이름이 Package 이름

# Package는 모듈의 집합

# Package 폴더가 정상적으로 Package 폴더로 동작하기 위해서는 안에 __init__.py 파일이 존재해야함.

# animal 패키지에서 dog 이라는 모듈을 갖고와
from Python.animal import dog 
from Python.animal import cat

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()