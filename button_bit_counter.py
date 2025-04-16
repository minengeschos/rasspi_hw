from gpiozero import LED, Button
from time import sleep

# 핀 설정 (LSB부터)
led_pins = [8, 7, 16]
leds = [LED(pin) for pin in led_pins]

button = Button(25, pull_up=True, bounce_time=0.1)

count = 0
prev_state = False  # 버튼이 안 눌린 상태

while True:
    curr_state = button.is_pressed  # True면 눌린 상태

    if curr_state and not prev_state:
        print(f"버튼 눌림: COUNT = {count}")

        # 3비트로 출력
        for j in range(3):
            bit = (count >> j) & 1
            if bit:
                leds[j].on()
            else:
                leds[j].off()

        count = (count + 1) % 8  # 0~7 반복
        sleep(0.2)  # 디바운싱

    prev_state = curr_state
    sleep(0.01)
