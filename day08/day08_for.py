# for 문
#
# for 변수 in 반복 객체:
#     반복 실행문 with 변수
#
# 반복 객체
# : 문자열, range(), 리스트, 튜플, 사전

# for 문자 in "Happy new year!":
#     print(문자, end="")

# 글자위치 = 0 # 인덱스
# 문자열 = "Happy new year!"
# 글자수 = len(문자열)
# while 글자위치 < 글자수:
#     print(문자열[글자위치])
#     글자위치 += 1

# 10번 반복하기
# for 횟수 in range(10):
#     print(횟수)

# 10번 반복하기 - 2
# for 횟수 in range(1, 11): # 1이상, 11 미만
#     print(횟수)

# 크리스마스 트리 출력하기
# for 문 이용
# print(공백 * 4 + 나무 * 1)
# print(공백 * 3 + 나무 * 3)
# print(공백 * 2 + 나무 * 5)
# print(공백 * 1 + 나무 * 7)
# print(나무 * 9)

# 공백 = " "
# # 1. 공백이 반복의 기준
# 나무개수 = 1
# 나무 = "#"
# for 공백개수 in range(4, -1, -1):  # 4부터 0까지(-1 전) 1씩 감소하는 것이 공백
#     print(공백 * 공백개수 + 나무 * 나무개수)
#     나무개수 +=2

# 2. 나무가 반복의 기준
# 공백 = " "
# 나무 = "#"
# 공백개수 = 4
# for 나무개수 in range(1,10, 2):  #1 부터 9까지(10 전) 2씩 증가하는 것이 나무
#     print(공백*공백개수 + 나무 * 나무개수 )
#     공백개수 -= 1

# 3. 각 줄의 공백과 나무 개수는 하나의 공식으로 표현할 수 있다.
# 공백개수 * 2 + 나무개수 = 9
# 나무개수 = 9 - 공백개수 * 2
#
# for 공백개수 in range(4, -1, -1):
#     print(공백 * 공백개수 + 나무 * (9 - 공백개수 * 2))

# 포함된 글자의 수 계산하기
인사말 = "merry christmas and happy new year"
a개수 = 0
for 한글자 in 인사말:
    if 한글자 == "a":
        a개수 += 1

print(a개수)

