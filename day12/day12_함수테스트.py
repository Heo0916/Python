# # 문제1. 돈을 넣으면 커피와 잔돈이 반환되는 "커피자판기" 함수를 구현하시오
# # 커피 한 잔은 300 이고, 뺄 수 있는 최대한 많은 커피를 뺀다.
#
#
# # 문제2. 사용자로부터 입력 받은 정수를 전달하면 해당 정수의 절대값이 리턴되는 "절대값" 함수를 구현하시오.
#
# # 문제1
# def 커피자판기(돈):
#     한잔 = 300
#     return 돈 // 한잔, 돈 % 한잔
#
# 커피, 잔돈 = 커피자판기(1400)
# print(커피)
# print(잔돈)
#
# 커피 = 커피자판기(5000)
# print(str(커피[0]) + "개의 커피와 남은 잔돈은 " + str(커피[1]) + "원입니다.")
#
# # 문제2
#
#
# def 절대값(정수):
#     if 정수 >= 0:
#         return 정수
#     else:
#         return 정수*(-1)
#
#
# 정수 = int(input("정수 입력 >>> "))
# 결과 = 절대값(정수)
# print(결과)




# 문제3. 돈을 넣으면 지금까지 쌓인 돈을 반환하는 "저금통" 함수를 구현하시오.

def 저금통(넣은돈):
    global 모은돈
    모은돈 += 넣은돈
    return 모은돈
모은돈 = 0
print(저금통(10000))
print(저금통(10000))
print(저금통(10000))
