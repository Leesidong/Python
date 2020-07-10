# 퀴즈

# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙 1: http:// 부분은 제외 => naver.com
# 규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"(!)로 구성

url = "http://naver.com"

my_str = url.replace("http://","")

index = my_str[:my_str.index(".")]

index = index[0:3]+str(len(index))+str(index.count("e"))+"!"

print(index)

# 1:22:00