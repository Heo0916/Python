

def 소개(이름, 나이):
    print("내 이름은 " + 이름 + "입니다.")
    print("내 나이는 " + str(나이) + "살입니다.")

print("자기 소개 시간입니다.")
소개("한남자", 15)
소개("한여자", 16)
소개("두남자", 20)
print("자기 소개를 마치겠습니다.")


def 신부증검사(나이): # 인수를 저장하는 변수를 매개 변수라고 한다.
    if 나이 >= 20:
        print("입장하세요.")
    else:
        print("못 들어 갑니다.")


신부증검사(15)
신부증검사(25)

