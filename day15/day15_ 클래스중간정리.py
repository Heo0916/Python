class Person:

    # 클래스 변수 (모든 Person 객체가 공유하는 변수)
    population = 0

    # 메서드(클래스 내부 함수 = 메서드)

    # 생성자(객체 생성 시 자동으로 호출되는 특별한 메서드 : 멤버 변수(self 변수, 인스턴스 변수) 초기화)
    def __init__(self, name, age, tall, weight="알 수 없음"):  # 매개 변수 : name, age, tall, weight(디폴트 매개 변수)
        self.name = name  # 인스턴스 변수 = 매개 변수
        self.age = age
        self.tall = tall
        self.weight = weight   # weight 를 받아 오면 받아온 값으로, 없으면 "알 수 없음"으로 사용
        # 인구 증가
        Person.population += 1

    # 소멸자(객체 소멸 시 자동으로 호출되는 특별한 메서드)
    def __del__(self): # 매개 변수를 지정하지 않음
        # 인구 감소
        Person.population -= 1

man = Person("철수", 20, 180.5, 80.5,)

woman = Person("영희", 21, 170.5)

print(Person.population)

del man # man 객체 소멸(소멸자 자동 호출)

print(Person.population)

