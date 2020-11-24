class Computer:

    def __init__(self):
        print("컴퓨터 생성 완료")


    def calculate(self):
        print("컴퓨터 계산중")

class Notebook(Computer):

    def __init__(self, battery):
        super(Notebook, self).__init__()
        self.battery = battery

    def charging(self):
        print("충전" + str(self.battery) + "완료")

lgcom = Computer()
gram = Notebook(70)

lgcom.calculate()
gram.calculate()
gram.charging()
