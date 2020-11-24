# 버튼 만드는 방법
#
# 버튼이름 = Button(창이름, text = "버튼에 표시할 텍스트", command = 함수이름)

from tkinter import *

숫자 = 0
def increment():
    global 숫자 # 전역 변수인 "숫자"를 사용한다.
    숫자 += 1
    label.config(text="현재 숫자 = " + str(숫자))  # 레이블 상태 갱신


window = Tk()

label = Label(window, text = "현재 숫자 = " + str(숫자))

button = Button(window, text="증가", command = increment)

label.pack()
button.pack()

window.mainloop()

