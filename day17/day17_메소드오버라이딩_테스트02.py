# 슈퍼 클래스 : Employee (기본급 받는 직원)
# 생성자 : salary 전달 (기본급)
# tax = salary 의 5% (모든 직원 공통)
# def pay : 기본급 출력
#
# 서브 클래스 : SalesWorker(기본급 + 판매수당)
# 생성자 : salary, total_Sales 전달(기본급, 판매실적)
# incentive = total_sales 의 20% (모든 판매직 공통)
# def pay : 기본급 출력 + 판매수당 출력


class Employee:
    # 클래스 변수
    tax_ratio = 0.05


    def __init__(self, salary):
        self.salary = salary
        self.tax = salary * Employee.tax_ratio


    def pay(self):
        print("기본급 = %d" %(self.salary-self.tax))


class SalesWorker(Employee):

    # 클래스 변수
    sales_ratio = 0.2

    def __init__(self,salary,total_Sales):
        # 슈퍼 클래스의 생성자 호출 다른 방
        # Employee.__init__(salary) (x)
        # super().__init__(salary) (0)
        super(SalesWorker, self).__init__(salary) #(0)
        #super().__init__(salary)  (0)
        self.total_Sales = total_Sales
        self.incentive = self.total_Sales * SalesWorker.sales_ratio

    def pay(self):
        super().pay()  # 기본급 출력
        print("판매수당 = %d" % (self.incentive * (1 - SalesWorker.tax_ratio)))

staff1 = Employee(300)
staff1.pay()

staff2 = SalesWorker(100, 1000)
staff2.pay()

