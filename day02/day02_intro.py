print("hello 파이썬")

# 1. 주석(comment)
# #으로 시작
# 쌍따옴표(") 3개, 홑따옴표(') 3개 사이에 주석 처리.

"""
여기도 주석으로 처리 될 부분
"""
# 파이참 자동 설정/해제 단축키 : ctrl + /(슬래시)

# 2. 출력 연습
#    1) 문자열 포맷 코드
#    (1) 문자열 : %s string 약자
#    (2) 정수  : %d decimal (10진수)
#    (3) 실수 :  %f floating point (부동 소수점)
#    2) format 함수를 이용한 출력
#       "문자열 사이에 {} 삽입".format(20)
#       "문자열 사이에 20 삽입"

print("나는 20살 입니다.")
print("나는 %d살입니다." %20)
print("내 성별은 %s입니다. " % "남자")
print("내 키는 %fcm 입니다. " %180.5)

print("나는 %d살 이고, 내 성별은 %s이고, 내 키는 %fcm 입니다." %(20, "남자", 180.5))

print("나는 %s살이고, 내 성별은 %s이고, 내 키는 %scm 입니다." %(20, "남자", 180.5))

print("서울시 마포구", "서교동") # 콤마(,)로 구분해서 출력하면 공백으로 구분해서 출력

print("나는 {}살 입니다.".format(20) )
print("내 성별은 {}입니다.".format("남자"))
print("내 키는 {0}cm이고, 내 몸무게는 {1}kg입니다.".format(180.5,85.5))
print("내 주소는 {addr}입니다.".format(addr="서울시 마포구 서교동"))

# print 사용하면 자동으로 줄 바꿈이 실행된다.
# 기본 값 : 출력의 마지막은 줄 바꿈이다.
# 기본값을 바꾸려면 end="" 속성을 지정한다.

# 월,화,수,목,금,토,일 출력하기
print("월", end=",") #월 출력 후에 콤마(,)를 출력한다.
print("화", end=",")
print("수")

# 빨주노초파남보 출력하기
print("빨", end="")
print("주", end="")
print("노")





