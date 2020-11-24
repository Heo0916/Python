# 클래스 변수
#
# 모든 객체(man, woman)들이 공유하는 변수

# 클래스 Person 을 구현하시오.

class Person():

    # 클래스 변수
    population = 0
    # 생성자 (생성할 때 자동으로 호출)

    def __init__(self, name ,age, hight, weight = "알 수 없음"):
        self.name = name
        self.age = age
        self.highet = hight
        self.weight = weight
        # Person 생성시 인구수 증가 (man, woman 생성될때마다 접근해서 1 증가되는 클래스 변수 population)
        Person.population += 1

    # 소멸자 ( 소멸할 때 자동으로 호출)
    def __del__(self):
        Person.population -= 1


    def show(self):
        print("이름 =", self.name)
        print("나이 =", self.age)
        print("키 =", self.highet)
        print("몸무게", self.weight)

man = Person("한남자" , 25, 180.5 , 80.5)
woman = Person("한여자" , 20, 170.5)

man.show()
woman.show()

del man # 객체 소멸( 소멸자가 자동으로 호출되는 시점)
