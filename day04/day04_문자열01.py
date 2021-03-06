# 문자열 string
# 1. 쌍따옴표(")와 홑따옴표(')를 모두 사용한다.
# 2. 여러 줄을  표현하려면 3개의 쌍따옴표(""")와 3개의 홑따옴표(''')를 모두 사용할 수 있다.
# 3. 이스케이프 문자 지원
#    1) \n : 줄 바꿈 (백슬래시 = 통화(원화) 기호)
#    2) \t : 탭 (간격을 맞출 때)
# 4. 문자열은 쌍따옴표(")를 주로 이용하기(다른 언어 예정)

# 문자열 연산자
# 1. + : 문자열 연결하기
# 2. * : 문자열 반복하기


문자열1 = "Hello"
문자열2 = 'Hello'
print(문자열1 == 문자열2)

# 히딩크는 "나는 아직 배고프다"라고 말했다.

print('히딩크는 "나는 아직 배고프다" 라고 말했다.')

#"히딩크는 '나는 아직 배고프다' 라고 말했다."
print("히딩크는 '나는 아직 배고프다' 라고 말했다.")

받는사람 = """
우편번호 12345
서울시 여의도구 여의도동 사서함 444
이병 홍길동
"""

print(받는사람)

보내는사람 = "우편번호 54321\n강원도 철원군 화천면 깡촌\n사랑하는 엄마"
print(보내는사람)

print("1\t10")
print("11\t10")
print("111\t10")

이름 = "루피"
주소 = "뽀롱뽀롱 마을"
자기소개 = 이름 + "는 " + 주소 + "에 삽니다." + str(20) + "살입니다." # str(20) : 정수 20을 문자열로 변환 함수
print(자기소개)

평점 = 5
print("★" * 평점)

# 크리스마스 트리 출력하기
    #
   ###
  #####
 #######
#########

# +, * 이용해서 출력
#내 생각
# print("\t" + "#")
# print("   " + "#" *3)
# print("  " + "#" *5)
# print(" " + "#" * 7)
# print("" + "#" * 9)

공백 = " "
나무 = "#"
print(공백 * 4 + 나무 * 1)
print(공백 * 3 + 나무 * 3)
print(공백 * 2 + 나무 * 5)
print(공백 * 1 + 나무 * 7)
print(나무 * 9)


