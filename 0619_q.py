# 과일이 들어 있는 리스트
x = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

# 안에 각 과일이 몇개씩 들어 있는 프로그램 만들기
d = {}

for f in x:
    if f in d:
        d[f] = d[f] +1
    else:
        d[f] = 1

print(d)