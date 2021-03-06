# if문
# 조건식을 만족하는 경우에만 실행하고 싶을 때
#
# 기본 형식
# if 조건식 :
#     실행문(True)
#     ...
# else:
#     실행문(Flase)
#     ...
# 확장 형식
# if 조건식:
#     실행문(True)
#     ...
# elif 조건식:
#     실행문(True)
#     ...
# else:
#     실행문(Flase)
#     ...
# 1. 실행문은 반드시 들여쓰기 후 작성한다.
# 2. 들여쓰기는 스페이스 4번(권장) 또는 탭 1번으로 한다.
# 3. 스페이스 4번과 탭 1번은 혼용할 수 없다.
# 4. else: 문은 생략할 수 있다.
# 5. elif 조건식: 문은 여러 개 추가할 수 있다.

# 문제1. 정수를 입력 받아 "정수" 변수에 저장하기.

# 문제2. 실수를 입력 받아 "실수" 변수에 저장하기.

# 정수 = int(input("정수 입력 >>>"))
#
# 실수 = float(input("실수 입력 >>>"))
#
# # 문제3. 이름을 입력 받아 "이름" 변수에 저장하기
# 이름 = input("이름 입력 >>> ")

# 정수를 입력 받아 양수는 "양수", 음수는 "음수", 0은 "0" 이라고 출력하기.

# 정수 = int(input("정수 입력 >>>"))
# if 정수 > 0:
#     print("양수")
# elif 정수 == 0:
#     print("0")
# else:
#     print("음수")

# 문제4. 두 정수를 입력 받아 그 중에서 큰수를 출력하라.

# 정수1 = int(input("첫번째 정수입력 >>>"))
# 정수2 = int(input("두번째 정수입력 >>>"))
#
# if 정수1 > 정수2:
#     print(정수1)
# else:
#     print(정수2)

# 문제5. 세 정수를 입력 받아 그 중에서 큰 수 출력하기
# 수1 = int(input("첫번째 정수입력 >>>"))
# 수2 = int(input("두번째 정수입력 >>>"))
# 수3 = int(input("세번째 정수입력 >>>"))

# if 수1>수2 and 수1>수3:
#     print(수1)
# elif 수2>수1 and 수2>수3:
#     print(수2)
# else :
#     print(수3)
#
#
# if 수1 > 수2:
#     if 수1> 수3:
#         print(수1)
#     else:
#         print(수3)
# else:
#     if 수2 > 수3:
#         print(수2)
#     else:
#         print(수3)
#
# 문제6. 실수 형태의 반지름을 입력 받아 원의 둘레와 원의 넓이를 구한 뒤, 그중에서 작은 값을 출력하기.
# import math
#
# 반지름 = float(input("반지름 입력 >>> "))
#
# 원의둘레 = math.pi * 2 * 반지름
# 원의넓이 = 반지름 ** 2 * math.pi * 2
#
# if 원의둘레 > 원의넓이:
#     print("원의둘레 = %f" %원의둘레)
# else:
#     print("원의넓이 = %s" %원의넓이)

# 문제7. 짝수, 홀수 구분하기
# 짝수 : 2, 4, 6, 8, , = 2로 나눈 나머지(%)가 0인 수
# 홀수 : 1, 3, 5, 7, , = 2로 나눈 나머지(%)가 1인 수

# 정수 = int(input("정수 >>> "))
# if 정수 % 2 == 0:
#     print("%d는 짝수" % 정수)
# else:
#     print("%d는 홀수" % 정수)

# 문제8. 3의 배수 여부 출력하기
# n의 배수 : n으로 나눈 나머지가 0인 수
# 정수 = int(input("정수 >>> "))
# if 정수 % 3 == 0:
#     print("%d는 3의 배수이다." % 정수)
# else:
#     print("%d는 3의 배수가 아니다." % 정수)
#
# 문제9. 정수를 입력(1~99) 받아서 3이 포함되어 있으면 1개 포함은 "짝" 출력, 2개 포함되어있으면 "짝짝" 출력

# 정수 = int(input("정수(1~99) 입력 >>> "))
# 몫 = 정수 // 10
# 나머지 = 정수 % 10
#
# if 몫 % 3 == 0 and 나머지 % 3 == 0:
#     print("짝짝")
# elif 몫 % 3 == 0 or 나머지 % 3 == 0:
#     print("짝")
# else:
#     print(정수)

# 문제10. 주민등록번호를 입력 받아 "남자", "여자" 구분해서 출력하기
# 주민등록번호의 8번째 글자가 홀수이면, "남자", 아니면 "여자"

주민등록번호 = input("주민등록번호 입력 >>> ")

if len(주민등록번호) == 14 and 주민등록번호.find("-") == 6:


    성별판별 = int (주민등록번호[7])
    if  성별판별 % 2 == 0 :
        print("여자")
    else:
        print("남자")

else:

    print("주민등록번호의 형식이 아닙니다.")










