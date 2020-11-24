# 이름(name)과 나이(age)를 가지는 사람(Person) 클래스를 구현하시오.
# 다음을 참고하시오.

# 구현
class Person:


    def show(self):
        print("이름 = %s , 나이 = %d " %(self.name, self.age))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age



man = Person("한남자" , 30)
woman = Person("한여자", 30)


man.show() # 이름 = 한남자, 나이 = 25
woman.show() # 이름 = 한여자, 나이 = 30



if man.get_age() > woman.get_age():
    print("남자가 연상입니다.")
elif man.get_age() == woman.get_age():
    print("동갑입니다.")
else:
    print("여자가 연상입니다.")
