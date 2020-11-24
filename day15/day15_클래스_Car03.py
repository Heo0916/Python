import datetime

# 자동차의 제조사 정보가 필요하다. 제조사가 한 군데라면?
# 모든 자동차에 제조사를 기억 시킬 필요는 없다.
# 클래스 변수를 활용할 것.


class Car:

    manufacturer = "현대"

    def __init__(self, model, color, year = datetime.datetime.now().year):
        self.model = model
        self.color = color
        self.year = year
        self.speed = 0
        self.power = False

    def __str__(self):
        message = "제조사 =" + Car.manufacturer + "\n모델 = " + self.model + "\n색상 =" + self.color + "\n년식 =" + str(self.year)
        return message


my_car = Car("람보르기니", "노랑")
print(my_car)  # print 를 통한 객체의 출력은 __str__ 메서드로 만든다.

your_car = Car("소나타", "검정", 2015)
print(your_car)