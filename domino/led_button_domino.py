from gpiozero import LED, Button
from signal import pause
from time import sleep

button = Button(25, pull_up=True, bounce_time=0.1)

led1 = LED(8)
led2 = LED(7)
led3 = LED(16)
led4 = LED(20)

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

button.when_pressed = start_domino

pause()
