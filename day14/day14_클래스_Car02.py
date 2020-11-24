import  datetime

class Car:

    power = False
    speed = 0
    model = ""
    color = "gray"
    year = 0

    def __init__(self, model, color, year=datetime.datetime.now().year):
# year = datetime.datetime.now().year  -> year 값이 전달되지 않으면 사용되는 기본 값(디폴트 매개 변수)
        self.model = model
        self.color = color
        self.year = year

    def show_car(self):
        print("모델 =", self.model)
        print("색상 =", self.color)
        print("년식 =", self.year)


my_car = Car("람보르기니", "노랑")  # __init__(self, model, color, year) 생성자 자동 호출, year 전달이 없어 디폴트 매개 변수가 사용됨
my_car.show_car()

your_car = Car("E-Class", "검정", 1990) # __init__(self, model, color, year) 생성자 자동 호출
your_car.show_car()