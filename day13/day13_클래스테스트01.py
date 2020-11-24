import math

class Circle: # 클래스명은 첫 글자를 대문자로 함.


    count = 0
    def __init__(self, name, rad):
        self.name = name
        self.radius = rad

        Circle.count += 1

    def show(self):
        print("이름 = %s, 반지름 = %s" %(self.name, self.radius))


    def get_area(self):
        return math.pi * self.radius ** 2




# 객체 생성 과정 (3개 객체 생성)
ball = Circle("농구공", 3.5)
pizza = Circle("페퍼로니" , 4.5)
ring = Circle("프로포즈반지" ,0.5)

ball.show()
pizza.show()
ring.show()

print("ball size = %s" % ball.get_area())
print("Pizza size = %s" % pizza.get_area())
print("ring size = %s" %ring.get_area())


print(Circle.count)   # 3



