# 클래스 Person 을 구현하시오.

class Person():

    # name = ""
    # age = 0
    # highet = 0
    # weight = 0

    def __init__(self, name ,age, hight, weight = "알 수 없음"):
        self.name = name
        self.age = age
        self.highet = hight
        self.weight = weight

    def show(self):
        print("이름 =", self.name)
        print("나이 =", self.age)
        print("키 =", self.highet)
        print("몸무게", self.weight)




man = Person("한남자" , 25, 180.5 , 80.5)
woman = Person("한여자" , 20, 170.5)

man.show()
# 이름 = 한남자
# 나이 = 25
# 키 = 180.5
# 몸무게 = 80.5

woman.show()
# 이름 = 한여자
# 나이 = 20
# 키 = 170.5
# 몸무게 = 알 수 없음


