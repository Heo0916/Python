# 엔트리 생성 방법
#
# 엔트리이름 = Entry(창이름)

from tkinter import *

def calc():
    # entry.get() : 텍스트 상자에 입력한 수식 읽어 오기
    # eval(문자열 형식의 수식) : 결과
    label.config(text= "수식 결과 = " + str(eval(entry.get())))



window = Tk()
window.title("나의 첫 번째 계산기")
window.resizable(False, False)

# 엔트리 생성
entry = Entry(window)

# 버튼 생성
button = Button(window, text="계산", command=calc)

# 레이블 생성
label = Label(window, text = "수식 결과가 나타날 위치")

entry.pack()
button.pack()
label.pack()

window.mainloop()