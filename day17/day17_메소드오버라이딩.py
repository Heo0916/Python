# 메서드 오버라이딩(Overriding)
#
# 슈퍼 클래스의 메서드 == 서브 클래스의 메서드
# 서브 클래스의 객체가 오버라이딩 된 메서드를 호출하면 서브 클래스의 메서드가 실행된다.
#
# 슈퍼 클래스 Person          - eat() 메서드
# 서브 클래스 Student         - eat() 메서드
# eat() 메서드가 오버라이딩(재 정의)된 상황
# 다시 만든(오버라이딩 된) 메서드가 실행된다.
#
# 서브 클래스 객체가 슈퍼 클래스 객체의 오버라이드 된 메서드를 호출하려면
# super().method()

class Person:

    def __init__(self, name):
        self.name = name
        self.meal = 0

    def eat(self):
        print("집에서 밥 먹는다.")

class Student(Person):

    def __init__(self, name, school):
        # 서브 클래스(Student)의 생성자는 반드시 슈퍼 클래스(Person)의 생성자 호출을 먼저 해야한다.
        # 슈퍼 클래스의 생성자 이름 :  super
        super(Student, self).__init__(name)
        self.school = school
        
    def eat(self):
        super().eat()  # super() -> Person, Person 의 eat() 메서드가 호출됨
        print("학교에서 밥 먹는다.")




man = Person("홍길동")
man.eat()

student = Student("한학생", "마포중")
student.eat()


