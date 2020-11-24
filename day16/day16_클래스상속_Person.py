# 상속(Inheritance)
#
# 1. 어떤 클래스가 가지고 있는 멤버들을 상속 받는 클래스가 사용할 수 있게 해 주는 것.
# 2. 일반적으로 IS-A 관계가 성립하면 상속 관계로 만들 수 있다.
#    예) 학생은 사람이다. 노트북은 컴퓨터이다. 전기차는 자동차이다. 개는 동물이다.
#
# 용어 정리
# 상속해주는 클래스    상속받는 클래스
# 슈퍼 클래스          서브 클래스
#
# 형식
#
# class 슈퍼 클래스:
#     본문
#
# class 서브 클래스(슈퍼 클래스):
#     본문

# 슈퍼 클래스
class Person:


    # 생성자
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " 밥을 먹는다. ")

    def sleep(self):
        print(self.name + " 잠을 잔다. ")


# 서브 클래스(Person 클래스의 멤버를 사용할 수 있는 Student 클래스)
class Student(Person):

    # 서브 클래스의 생성자 작성 방법
    # 1. 반드시 슈퍼 클래스의 생성자를 먼저 호출해야 한다.
    #    슈퍼 클래스 호출 : super(서브 클래스, self).__init__()
    # 2. 자신의 인스턴스 멤버를 초기화한다.
    def __init__(self, name, school ):
        # Person(name) 과 같은 방식
        super(Student, self).__init__(name)
        self.school = school

    def study(self):
        print(self.name + "가 " + self.school + "에서 공부를 한다.")


# Person 객체 생성
pororo = Person("뽀로로")
pororo.eat()
pororo.sleep()

harry = Student("해리포터", "호그와트")
harry.eat()
harry.sleep()
harry.study()



