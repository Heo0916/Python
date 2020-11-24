# 채널(channel)과 볼륨(volume)과 전원(power)을 가지는 TV 클래스를 구현하시오.


class TV:

    # 클래스 변수
    MAX_CH = 5
    MIN_CH = 1
    MAX_VOL = 5
    MIN_VOL = 0

    def __init__(self, ch, vol, power):
        self.channel = ch
        self.volume = vol
        self.power = power

    def power_button(self, signal):
        self.power = signal
        if self.power:  # if signal == True:
            print("전원 켜졌다.")
        else:
            print("전원 꺼졌다.")

    def showChannel(self):
        print("채널 = %d" % self.channel)

    def showVolume(self):
        print("볼륨 = %d" % self.volume)

    def incrementCh(self):
        # if self.channel == TV.MAX_CH:
        #     self.channel = TV.MIN_CH
        # else:
        #     self.channel += 1
        # incrementCh() 함수는 한 줄로 가능합니다.
        self.channel = (self.channel + 1) % TV.MAX_CH

    def incrementVol(self):
        if self.volume != TV.MAX_VOL:
            self.volume += 1


my_tv = TV(1, 1, False)

my_tv.power_button(True)  # 전원 켜졌다.

my_tv.showChannel()  # 채널 = 1
my_tv.showVolume()   # 볼륨 = 1

for 횟수 in range(10):  # 10번 반복
    my_tv.incrementCh()
    my_tv.showChannel()  # 채널 = 2 -> 3 -> 4 -> 5 -> 1 -> 2 -> 3 ...

for 횟수 in range(10):  # 10번 반복
    my_tv.incrementVol()
    my_tv.showVolume()  # 볼륨 = 2 -> 3 -> 4 -> 5 -> 5 -> 5 -> 5 ...

my_tv.power_button(False)  # 전원 꺼졌다.
