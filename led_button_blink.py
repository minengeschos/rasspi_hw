from gpiozero import LED, Button
from signal import pause

# 버튼과 LED 핀 설정
button = Button(25, pull_up=True)  # 내부 풀업 활성화
leds = [LED(8), LED(7), LED(16), LED(20)]

# 버튼이 눌렸을 때 LED ON
def turn_on():
    for led in leds:
        led.on()

# 버튼이 떼졌을 때 LED OFF
def turn_off():
    for led in leds:
        led.off()

# 이벤트 연결
button.when_pressed = turn_on
button.when_released = turn_off

# 종료 방지 (무한 대기)
pause()
