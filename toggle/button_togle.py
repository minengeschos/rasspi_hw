from gpiozero import LED, Button
from signal import pause
from time import sleep

# 버튼과 LED 설정
button = Button(25, pull_up=True, bounce_time=0.2)
leds = [LED(8), LED(7), LED(16), LED(20)]

# LED 상태 저장 (리스트로 감싸서 함수 안에서 수정 가능하게 함)
led_state = [False]

# 버튼이 눌렸을 때 실행할 함수
def toggle_leds():
    led_state[0] = not led_state[0]
    for led in leds:
        if led_state[0]:
            led.on()
        else:
            led.off()
    print("LED 상태:", "ON" if led_state[0] else "OFF")

# 버튼 이벤트 핸들러 연결
button.when_pressed = toggle_leds

# 프로그램을 계속 실행 상태로 유지
pause()
