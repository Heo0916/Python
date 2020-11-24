# 예외 처리(에러 처리)
#
# 예외 처리 문법
#
# try:
#     예외가 발생하는 구역
#
# except:
#        예외가 발생한 경우 실행되는 구역
# else:
#      예외가 발생하지 않은 경우 실행되는 구역
# finally:
#         무조건 실행되는 구역

# try:
#     a = 10
#     b = 5
#     div_result = a / b
#     print("%d / %d = %d" % (a, b, div_result))
#
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")


# try:
#     a = int(input("정수 1 입력 >>>"))
#     b = int(input("정수 2 입력 >>>"))
#     add_result = a + b
#     print("%d + %d = %d"  % (a, b, add_result))
# # 입력이 정수가 아닌 경우 정수형으로 변경하려고 할 때
# except ValueError:
#     print("연산 할 수 없는 값이 사용되었습니다.")
# # 서로 연산할 수 없는 자료형으로 연산하려고 할때(예 : 정수+ 문자열
# except TypeError:
#     print("연산 할 수 없는 값이 사용되었습니다.")

try:
    리스트 = [1, 2, "삼"]
    print(리스트[5])
except IndexError as e:
    print(e)

