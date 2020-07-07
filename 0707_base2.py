# 문자열

sentence = '나는 소년 입니다'

print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)


# """ <- 줄 바꿈
sentence3 ="""
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)


# 슬라이싱
jumin = "990120-1234567"

# substring 하는 법
# : 없을 경우 하나만 가져오고 있을 경우 직전까지
print("성별 : "+ jumin[7])
print("연 : " +jumin[0:2])

print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

# : 앞에 안쓸 경우 처음부터 가져옴
print("생년월일 : " + jumin[:6])

# : 뒤에 안쓸 경우 끝까지 가져옴
print("뒤 7자리 : " +jumin[7:])

# 뒤에서 부터 카운트 하기 때문에 -1 부터 시작
# -7이기 때문에 뒤에 7번째부터 시작
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])

# 55:10
