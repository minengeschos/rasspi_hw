youtube: https://youtu.be/ycMFObPjUn8

# Raspberry Pi Domino LED Sequence with Button

이 프로젝트는 Raspberry Pi에서 버튼을 누르면 **LED들이 도미노처럼 순서대로 켜졌다가 꺼지는 효과**를 보여주는 예제입니다.

## 기능 설명

- 버튼을 누르면 4개의 LED가 **순서대로 하나씩 켜지고**,  
  각 LED는 1초간 켜진 후 꺼집니다.
- LED는 마치 도미노가 넘어지듯 **차례로 반응**합니다.
- 버튼은 풀업 방식으로 연결되며, 디바운싱 설정이 적용되어 있어 **노이즈 없이 안정적으로 감지**됩니다.

## 핀 연결

| 기능     | GPIO 핀 번호 |
|----------|--------------|
| 버튼     | GPIO 25      |
| LED 1    | GPIO 8       |
| LED 2    | GPIO 7       |
| LED 3    | GPIO 16      |
| LED 4    | GPIO 20      |

**참고:** 버튼의 한쪽은 GND(접지)에 연결되어야 합니다.

## 코드 설명

```python
from gpiozero import LED, Button
from signal import pause
from time import sleep

# 버튼 설정 (풀업 저항 사용, 디바운싱 시간 0.1초)
button = Button(25, pull_up=True, bounce_time=0.1)

# LED 설정
led1 = LED(8)
led2 = LED(7)
led3 = LED(16)
led4 = LED(20)

# 버튼 눌렀을 때 실행될 함수
def start_domino():
    print("버튼 눌림 감지! 도미노 시작")

    led1.on()
    sleep(1)
    led1.off()

    led2.on()
    sleep(1)
    led2.off()

    led3.on()
    sleep(1)
    led3.off()

    led4.on()
    sleep(1)
    led4.off()

# 버튼 이벤트 연결
button.when_pressed = start_domino

# 프로그램 종료 방지 (계속 대기)
pause()
