#함수 Funsion

def chat(name1, name2,age):
    print(name1 + " : 안녕?  넌 몇 살이니?")
    print(name2 + " : 나? 나는 "+str(age))
    print("%s : 나? 나는 %d" %(name2,age) )

chat("알렉스","윤하",2)

chat("철수","영희",20)


# 반환값 던지기
def dsum(a,b):
    result = a+b
    return result


c = dsum(1,2)

print(c)


# 반복문 (for, while)

for i in range(5):
    print(i)
    print("반복반복")

i = 0

while i<3:
    print(i)
    print("While 반복")
    i=i+1


#break, continue
i=0

while True:
    print(i)
    print("무한 루프")

    i = i +1

    if i>2:
        break


for i in range(3):
    print(i)
    print("Continue")

    continue

    print("안나와")

#37:21
