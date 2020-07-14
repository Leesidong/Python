# 자료구조의 변경

# 커피숍이라는 집합
menu = {"커피","우유","주스"}
print(menu ,type(menu))
# type으로 찍을 경우 menu를 집합 set 형식으로 넣었기 때문에 set이 나옴

# set을 변경
menu = list(menu)
print(menu, type(menu))
# list로 감싸서 변경했기 때문에 list로 타입 변경

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu,type(menu))