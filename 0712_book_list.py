# 리스트
# 대괄호로 생성

# 초기 생성 시 값이 없는 리스트 선언
data = list()
data_init = []

# 초기 생성 시 값이 있는 리스트 선언
# 숫자만 있는 리스트
odd = [1, 3, 5, 7, 9]

# 문자만 있는 리스트
stringData = ['a', 'b', 'c', 'd']

# 숫자와 문자가 같이 있는 리스트
totalData = [1, 3, 5, 'a', 'b', 'c']

# 리스트 안에 또다른 리스트가 있는 리스트
list_init = [1, 2, 'a', 'b', totalData]
list_init_2 = [1, 2, 'a', 'b', [3, 4, 'c', 'd']]

# list_init_2 에서 list_init_2[-1] 출력시
# [3,4,'c','d']가 출력이 된다.
print(list_init_2[-1])

# 만약 list_init_2[-1]에서 출력되는 값 [3, 4, 'c', 'd'] 에서
# 'c'의 값을 출력하고 싶을 경우
# list_init_2[-1]에서 'c'의 값이 [2]또는 [-2]이기 때문에
# list_init_2[-1][2]로 출력이 가능
print(list_init_2[-1][2])
print(list_init_2[-1][-2])

# 리스트를 3중으로도 사용이 가능

list_test = [1, 2, ['a', 'b', ['Life', 'is']]]

print(list_test)

# 이때 'Life' 값을 출력하고 싶을 경우
print(list_test[-1][-1][0])

a = [1, 2, 3, 4, 5]
b = a[1:3]
print("A = ", b)

# 리스트 관련 함수
# del 객체
# 리스트에서 리스트 요소 삭제
a = [1,2,3]
del a[1]
# del a[2:] 로도 사용 가능
print(a)

# append()
# 리스트의 마지막에 값을 추가
a = [1,2,3]
print(a)

a.append(4)
print(a)

# 추가를 할때 리스트로 추가 가능
a.append([4,5])
print(a)

# sort()
# 리스트의 값을 정렬
a = [1,4,3,2]
a.sort()
print(a)

# reverse
# 리스트의 값을 역순으로
# 리스트의 값을 정렬하여 역순으로 뒤집는 것이 아닌
# 그냥 순수 리스트의 값을 그냥 역순으로 해버림.
a = ['a','b','c']
a.reverse()

print(a)

# index
# 해당 인덱스에 값이 있을 경우 해당 값을 반환.
a = [1,2,3]
b = a.index(2)

print(b)

# 만약 값이 없을 경우에는 에러가 발생함.
# 4c = a.index(4)
# print(c)

# insert
# index에 값을 집어 넣을 경우
a = [1,2,3]

# index 0에 4를 넣었기 때문에 1,2,3은 한칸씩 밀림
a.insert(0,4)

print(a)

# remove
# 리스트 안에 있는 값을 삭제 할 경우
# index의 값이 아닌 실제 값을 삭제
a = [1,2,3]
a.remove(1)

print(a)

# pop
# 리스트 요소의 값을 꺼내서 출력 후 삭제
a = [1,2,3]

print("꺼낸 값 : " + str(a.pop(1)))

print(a)

# count
# 리스트 안에 요소가 몇개인지 확인
a = [1,2,3,4]

print(a.count(2))

# 리스트의 길이를 사용할때 len를 사용해서 길이를 확인 해야하며
# count 로는 리스트 길이를 확인할 수 없음.
print(len(a))

# extend
# 리스트와 리스트를 더할 경우
# 리스트와 리스트를 더할 때 사용하기 때문에 괄호 안에는 리스트 만 사용 가능함.

a= [1,2,3]
b = [4,5]

a.extend(b)

print(a)

# 먄약 extend 안에 리스트가 아닌 값을 넣을 경우 에러 발생
# a.extend(1)

# print(a)