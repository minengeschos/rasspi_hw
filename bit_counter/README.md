youtube: https://youtu.be/R1r4cjsGSH4

# Raspberry Pi 3-Bit LED Counter with Button

이 프로젝트는 라즈베리파이의 GPIO를 이용해 **버튼을 누를 때마다 3개의 LED로 0부터 7까지 숫자를 2진수로 표시**하는 예제입니다.

## 기능 설명

- 버튼을 누를 때마다 숫자가 1씩 증가합니다.  
- 숫자는 3개의 LED로 이진수 형태로 출력됩니다.  
- 숫자는 0부터 시작해 7까지 올라가고, 그 다음 다시 0으로 되돌아갑니다.

## 핀 연결

| 기능     | GPIO 핀 번호 |
|----------|--------------|
| LED 1 (LSB) | GPIO 8     |
| LED 2      | GPIO 7     |
| LED 3 (MSB) | GPIO 16    |
| 버튼       | GPIO 25    |

## 코드 설명

```python
from gpiozero import LED, Button
from time import sleep

# LED 핀 번호를 LSB부터 지정
led_pins = [8, 7, 16]
leds = [LED(pin) for pin in led_pins]

# 버튼 설정 (풀업 저항, 디바운싱 시간 포함)
button = Button(25, pull_up=True, bounce_time=0.1)

count = 0  # 현재 숫자
prev_state = False  # 이전 버튼 상태

while True:
    curr_state = button.is_pressed  # 현재 버튼 상태

    if curr_state and not prev_state:
        print(f"버튼 눌림: COUNT = {count}")

        # count를 3비트 이진수로 LED에 출력
        for j in range(3):
            bit = (count >> j) & 1
            if bit:
                leds[j].on()
            else:
                leds[j].off()

        # 숫자 증가 (0~7에서 반복)
        count = (count + 1) % 8
        sleep(0.2)  # 디바운싱 보조

    prev_state = curr_state
    sleep(0.01)  # 반복 간 간격
