# Label : 텍스트 표시 또는 이미지 표시
#
# 1. 텍스트 표시 방법
# 레이블이름 = Label(창이름, text="표시할 텍스트")
#
# 2. 이미지 표시 방법
#     1) 이미지 생성
#        이미지이름 = PhotoImage(file="이미지파일")
#     2) 이미지 표시
#        레이블이름 = Label(창이름, image=이미지이름)
#
# 3. 컨테이너 화면 표시 방법
#    1) pack : 그냥 알아서 배치
#    2) grid : 격자(표)
#    3) - 행(row), 열(column)
#        column = 0 column = 1 column = 2
# row = 0
# row = 1
# row = 2

from tkinter import *
from random import randint

# randint(1, 10) : 1~10 사이 난수 생성

window = Tk()

# 레이블 생성 (레이블이름 : label1 - 임의로 결정)
label1 = Label(window, text = "안 내면 진 거")

# 레이블 배치
label1.grid(row=0, column = 0)

# 레이블 생성 (레이블이름 : label1 - 임의로 결정)
label2 = Label(window, text = "가위 바위 보")

# 레이블 배치
label2.grid(row=0, column = 1)

# player1 랜덤 생성
player1 = randint(1, 3)

# 이미지 생성
photo1 = PhotoImage(file="./File/" + str(player1) + ".gif") # . : 현재 소스 파일이 존재하는 폴더(현재 폴더)

# 이미지를 레이블에 배치
label3 = Label(window, image = photo1)

# 레이블 배치 (grid)
label3.grid(row=1, column = 0)

# player2 랜덤 생성
player1 = randint(1, 3)

# 이미지 생성
photo2 = PhotoImage(file="./File/" + str(player1) + ".gif") # . : 현재 소스 파일이 존재하는 폴더(현재 폴더)

# 이미지를 레이블에 배치
label4 = Label(window, image = photo2)

# 레이블 배치 (grid)
label4.grid(row=1, column = 1)
window.mainloop()
