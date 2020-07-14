# 집합 (set)

# 중복 안됨, 출력 순서 없음
my_set = {1,2,3,3,3}
# 딕셔너리와 동일하게 중괄호를 쓰지만
# 다른 점은 키 값을 안씀.

print(my_set)

java = {"유재석", "김태호","양세형"}

python  = set(["유재석","박명수"])

# 자바와 파이썬 중복이 유재석임
# 교집합 출력
# 자바와 파이썬 둘다 가능

print(java & python)
print(java.intersection(python))
# 두개가 동일함.

# 합집합
print(java | python)
print(java.union(python))

# 차집합
# java는 할줄 알고 python은 못하는 사람
print(java - python)
print(java.difference(python))

# python에 값 추가
python.add("김태호")
print(python)

# java 값 빼기
java.remove("김태호")
print(java)