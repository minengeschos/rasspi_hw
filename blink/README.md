# Raspberry Pi Button-Activated LED Control

이 프로젝트는 Raspberry Pi에서 **버튼을 누르면 여러 개의 LED가 켜지고**,  
**버튼에서 손을 떼면 LED가 꺼지는 간단한 회로 및 코드 예제**입니다.

## 기능 설명

- 버튼을 누르고 있는 동안 4개의 LED가 모두 켜집니다.
- 버튼에서 손을 떼면 LED가 꺼집니다.
- `gpiozero` 라이브러리를 사용하여 코드를 간단하게 구성했습니다.

## 핀 연결

| 기능     | GPIO 핀 번호 |
|----------|--------------|
| 버튼     | GPIO 25      |
| LED 1    | GPIO 8       |
| LED 2    | GPIO 7       |
| LED 3    | GPIO 16      |
| LED 4    | GPIO 20      |

**주의:** 버튼은 풀업 연결(pull-up) 방식으로 사용됩니다. 따라서 **한쪽은 GND에 연결**해야 합니다.

## 코드 설명

```python
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
