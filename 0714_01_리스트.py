# 리스트

subway = [10,20,30]

print(subway)

# 기본 리스트 출력
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 리스트 내의 인덱스 확인
print(subway.index("조세호"))

# 마지막에 리스트 추가
subway.append("하하")
print(subway)

# 원하는 인덱스에 값 추가
subway.insert(1,"정형돈")
print(subway)

# 마지막 값 빼기
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명인지
subway.append("유재석")
print(subway)

print(subway.count("유재석"))


# 정렬 하는 법
num_list = [2,3,1,5,4]
print(num_list)

num_list.sort()
print(num_list)

# 순서 뒤집기 역 출력
num_list.reverse()
print(num_list)

# 리스트 안에 데이터 지우기
num_list.clear()
print(num_list)