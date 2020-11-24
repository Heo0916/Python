# 클래스 (class)
#
# 서로 관련 있는 변수와 함수를 모아 놓은 구조
# 클래스를 정의하고(설계도를 만들고) 객체를 생성하여(실제로 만든 데이터) 사용한다.
#
# 클래스 정의(클래스 구현)
# class 클래스명:
#     멤버 변수
#     def 멤버 함수(메서드)
#
# 객체 생성 과정
# 객체명 = 클래스명()


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):  # 모든 멤버함수(메서드)는 반드시 self 를 첫 번째 인수로 가져야 한다.
        print("[%d, %d]" %(self.x, self.y))


my_dot = Point(5, 10)  # my_dot 객체
my_dot.show()  # x, y 좌표 출력


