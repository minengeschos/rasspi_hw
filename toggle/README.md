youtube: https://youtu.be/yLl51VmMHkk

# Raspberry Pi Button Toggle LED Control

이 프로젝트는 Raspberry Pi에서 **하나의 버튼으로 여러 개의 LED를 ON/OFF 전환(toggle)하는** 예제입니다.

## 기능 설명

- 버튼을 **한 번 누르면 모든 LED가 켜지고**,  
  **다시 누르면 모든 LED가 꺼지는 방식**입니다.
- 매번 버튼을 누를 때마다 LED의 상태가 반전(toggle)됩니다.
- 디바운싱 기능을 적용해 버튼 입력의 안정성을 높였습니다.

## 핀 연결

| 기능     | GPIO 핀 번호 |
|----------|--------------|
| 버튼     | GPIO 25      |
| LED 1    | GPIO 8       |
| LED 2    | GPIO 7       |
| LED 3    | GPIO 16      |
| LED 4    | GPIO 20      |

> 버튼은 풀업 방식으로 연결되며, 한쪽은 GND에 연결되어야 합니다.

## 코드 설명

```python
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
