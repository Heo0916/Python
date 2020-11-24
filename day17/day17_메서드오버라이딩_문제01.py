class Car:


    def drive(self):
        print("4 바퀴가 굴러간다.")

class EV(Car):

    def drive(self):
        print("전기로" ,end="")   # EV 만의 특징
        super().drive()           # Car 의 기능을 포함



car = Car()
ev = EV()

car.drive()
ev.drive()