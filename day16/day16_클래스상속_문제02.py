class Employee:

    def __init__(self, name):
        self.name = name

class SalaryMan(Employee):

    def __init__(self, name, salary):
        super(SalaryMan, self).__init__(name)
        self.salary = salary

    def pay(self):
        print(self.name + " 월급 %d" %self.salary )

class Alba(Employee):

    def __init__(self, name, time, money):
        super(Alba, self).__init__(name)
        self.time = time
        self.money = money

    def pay(self):
        print(self.name +" 월급 "+ str(self.money * self.time))


staff1 = SalaryMan("김직원", 200)
staff2 = Alba("박알바", 100, 1.5)

staff1.pay() # 김직원 월급 200
staff2.pay() # 박알바 월급 150
