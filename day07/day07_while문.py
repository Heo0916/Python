# while 문
# 조건식을 만족하면 계속 실행한다.
#
# while 조건식:
#     실행문
#     ...

# "Hello" 5번 출력하기(pring("Hello") 5번 실행하기)
# 개수 = 1
# while 개수 <= 5:
#     print("Hello")
#     개수 = 개수 + 1 # 개수 += 1


# 개수 = 5
# while 개수 >= 1:
#     print("Hello")
#     개수 = 개수 - 1 # 개수 -= 1

# # 1~5 정수 출력하기
# 정수 = 1
# while 정수 <= 5:
#     print(정수, end=" ")
#     정수 = 정수 + 1

# 5 ~ 10 사이 정수 출력하기
# 정수 = 5
# while 정수 <= 10:
#     print(정수, end=" ")
#     정수 += 1
#
# print()
# # 10 ~ 1 사이 역순 정수 출력하기
# 정수1 = 10
# while 정수1 >= 1:
#     print(정수1,end=" ")
#     정수1 -= 1

# 1 ~ 20 사이의 모든 짝수 출력하기
# if 문은 사용하지 말기

# 정수 = 2
# while 정수 <= 20 :
#     print(정수, end=" ")
#     정수 += 2

# 문제1. 사용자로부터 양수를 입력 받아,
# 그 수만큼 "안녕하세요"를 출력하는 프로그램을 구현

# 양수 = int(input("양수를 입력하세요 >>> "))
# 개수 = 1
#
# while 개수 <= 양수:
#     print("안녕하세요")
#     개수 += 1

# 양수 = int(input("출력 횟수 입력 >>> "))
# while 양수 >= 1:
#     print("안녕하세요")
#     양수 = 양수 - 1

# 문제2. 사용자로부터 양수를 입력 받아,
# 1부터 양수까지 모든 정수를 출력하기.

# 양수 = int(input("양수 입력 >>> "))
# 정수 = 1
#
# while 정수 <= 양수:
#     print(정수, end=" ")
#     정수 += 1

# 문제3. 사용자로부터 출력하고 싶은 구구단을 입력 받아
# 해당 구구단을 출력하는 프로그램
# 예: 구구단 입력 >>> 2
# 2 * 1 = 2

# 구구단 = int(input("구구단 입력 >>> "))
# 정수 = 1
# while 정수 <= 9:
#     print("%d X %d = %d " %(구구단, 정수, 구구단*정수))
#     정수 = 정수 + 1


# 문제4. 1~100 사이 모든 정수를 검사하여,
# 7의 배수(7로 나눈 나머지가 0인 수)만 출력하는 프로그램

# 정수 = 1
# while 정수 <= 100 :
#     if 정수 % 7 == 0:
#         print(정수)
#     정수 += 1

# 문제5. 1 ~ 1000 사이 모든 정수를 검사하여,
# 짝수만 출력하기
# 한 줄당 10개의 짝수만 출력하기.

# 정수 = 1
# count = 0
# while 정수 <= 1000 :
#     if 정수 %2 == 0:
#         if count % 10 == 0:
#             print("")
#         print(정수, end="\t") # 정수 출력 후 탭 이동(정수 길이가 달라도 같은 탭 간격으로 이동)
#         count += 1
#     정수 = 정수 + 1

정수 = 1
while 정수 <= 1000:
    if 정수 % 2 == 0:
        print(정수, end="\t")
        if 정수 % 20 == 0:
            print("") # 줄 바꿈
    정수 = 정수 + 1








