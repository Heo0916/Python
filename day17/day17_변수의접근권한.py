# 접근권한

# private : 나(클래스) 만 쓸 수 있다.
# 변수 이름이 __(언더바 2개) 로 시작하면 private 권한
#
# public : 누구나 쓸 수 있다.
# 변수 이름이 _(언더바) 로 시작하지 않으면 public 권한

class Parent:

    def __init__(self, a):
        self.__a = a    # self.__a : private 하기 때문에 오직 Parent 객체만 사용할 수 있다.

    def get_a(self):
        return self.__a


class Child(Parent):

    def __init__(self, a, b):
        super(Child, self).__init__(a)
        self.__b = b

    def show_member(self):
        print(self.get_a())  # __a 는 private 이라서 직접 볼 수 없으므로 대신 보여주는 메서드 get_a() 를 이용한다.


boy = Child(1, 2)
boy.show_member()

