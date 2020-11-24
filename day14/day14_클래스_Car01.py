import datetime


class Car:

    power = False  # self.power
    speed = 0      # self.speed
    model = ""     # self.model
    color = "gray" # self.color
    year = datetime.datetime.now().year  # self.year

    def power_button(self, signal):
        if signal: # signal == True:
            self.power = True
            print("시동 켜졌습니다.")
        else:
            self.power = False
            print("시동 꺼졌습니다.")
            self.speed = 0

    def drive(self, speed):
        self.speed = speed

# 클래스를 통해 만들어진 실제 객체 생성
# 객체이름 = 클래스이름()

my_car = Car()               # 자동차 만들어 진 곳

my_car.model = "람보르기니"   # 이미 만들어 진 자동차가 "람보르기니"라고 나중에 정한 경우
my_car.color = "노란색"       # 이미 만들어 진 자동차가 "노랑"이라고 나중에 정한 경우

my_car.power_button(True)
my_car.drive(50)
my_car.power_button(False)

print("모델 =", my_car.model)
print("색상 =", my_car.color)
print("연식 =", my_car.year)
print("속도 =", my_car.speed)

