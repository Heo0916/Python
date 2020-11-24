# 생성자 (Constructor)
#
# 1. 객체가 생성될 때 자동으로 호출되는 메서드이다.
# 2. 생성자의 모습 : __init__(self, , , )


class Point:

    x = 0   # self.x
    y = 0   # self.y

    def __init__(self, xxx, yyy):
        self.x = xxx
        self.y = yyy
        print("생성자 호출")

    def show(self):
        print("[%d, %d]" % (self.x, self.y))


center = Point(10, 12) # 생성시 10, 12로 초기화 -> 생성자에게 10, 12를 전달 -> __init__ 메서드가 자동으로 호출됨
center.show()   # show() 메서드 호출

