# tkinter : 파이썬 GUI 모듈
# ( 주의 : 파이썬 2.X (TKinter), 파이썬 3.X (tkinter)
#
# 기본 구성
# 객체이름 = Tk()  # 객체 생성 (window 생성)
# 컨트롤 배치
# 객체이름.mainloop()   # 이벤트 루프 생성 (window 화면에 나타남)

# 모듈 포함 1
# import  tkinter
# 내창 = tkinter.Tk()

# 모듈 포함 2
#from tkinter import *  # tkinter 모듈의 모든 것을 사용하겠다.
#내창 = Tk()            # tkinter. 을 매번 적을 필요가 없다.

from tkinter import *

# 1. window 생성(객체이름 : window, 임의로 결정)
window = Tk()

# 2. 창 제목
window.title("내가 만든 첫 번째 창")

# 3. 크기 위치 결정 (안하면 기본 값)
window.geometry("1024x768+200+100")

# 4. 크기 조절 유무
window.resizable(True, True)  # resizable(가로, 세로)  크기 변경이 가능한 상태

# 5. window 이벤트 루프
window.mainloop()

























