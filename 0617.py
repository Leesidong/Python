print("Hello World")

# 변수

x = 1
y = 2

print(x)
print(y)

a = "안녕"
print(a)

z = 1.2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)

x = "hello"
y = 'hello'

z = """
안녕하세요
안녕하세요
"""
print(x)
print(y)
print(z)

x = 4
y = "4"

# 정수를 문자 캐스팅
print(str(x)+y)

# 문자를 정수 캐스팅
print(x+int(y))



# 조건문
# if ~ else

if not 0>1 :
    print("hello")


if 1>0 and 2>1:
    print("ha")


if 0>0 or 2>1:
    print("a")


x = 3

if x>5:
    print("hee")
else:
    print("hi")

if x>5:
    print("aaa")
elif x==3:
    print("bbb")
else:
    print("ccc")