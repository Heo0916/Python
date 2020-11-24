# Car 클래스의 기능
#
# 1. 최저 속도 = 0 상수 선언(상수 선언 방법이 없다.)
# 2. 최고 속도 = 100 상수 선언(이름을 대문자로 주는 것뿐!)
# 3. power_button() : True 전달 시 power 가 True, False 전달 시 power 가 False
# 4. gas_station() : 전달이 없으면 fuel = 10(full), 전달이 있으면 전달한 만큼 fuel 저장
# 5. accelerator() : speed 가 10 증가, fuel 는 1 감소
# 6. brake() : speed 가 10 감소, fuel 는 영향 없음.
# 7. panel_info() : 현재 speed 하고, 남은 fuel 확인
# 8. fuel 의 초기값은 5로 한다.
import datetime


class Car:

    manufacturer = "BMW"
    MAX_SPEED = 100
    MIN_SPEED = 0
    MAX_FUEL = 10

    def __init__(self, model, color, year = datetime.datetime.now().year):
        self.model = model
        self.color = color
        self.year = year
        self.speed = 0
        self.power = False
        self.fuel = 5

    def __str__(self):
        message = "제조사 =" + Car.manufacturer + "\n모델 = " + self.model + "\n색상 =" + self.color + "\n년식 =" + str(self.year)
        return message

    def power_button(self, power):
        if power:       # if 파워 == ture:
            self.power = True
        else:
            self.power = False

    def gas_station(self, fuel = 10):
        self.fuel += fuel
        if self.fuel > Car.MAX_FUEL:
            self.fuel = Car.MAX_FUEL

    def accelerator(self):
        if not self.fuel:
            print("연로 부족!")
        elif self.speed == Car.MAX_SPEED:  # 최대 속도일 경우
            self.fuel -= 1
        else:
            self.speed += 10
            self.fuel -= 1

    def brake(self):
        if self.speed == Car.MIN_SPEED:  # 최저 속도(0)인 경우
            print("멈췄다.")
        else:
            self.speed -= 10

    def panel_info(self):
        print("현재 속도 : %d, 남은 연료 : %d" % (self.speed, self.fuel))


bmw = Car("520d", "검정")
for 횟수 in range(5):
    bmw.accelerator()

bmw.panel_info()
bmw.gas_station(100)
bmw.panel_info()

for 횟수 in range(10):
    bmw.accelerator()

bmw.panel_info()

for 횟수 in range(11):
    bmw.brake()

bmw.panel_info()



