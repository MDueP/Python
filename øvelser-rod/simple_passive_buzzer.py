from machine import Pin
from machine import PWM
from time import sleep

BUZZ_PIN = 26
buzzer_pin = Pin(BUZZ_PIN, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)

def buzzer(buzzer_PWM_object, frequency, sound_duration, silence_duration):
    buzzer_PWM_object.duty(512)
    buzzer_PWM_object.freq(frequency)
    sleep(sound_duration)
    buzzer_PWM_object.duty(0)
    sleep(silence_duration)
buzzer(pwm_buzz, 262, 0.2, 0.2)
buzzer(pwm_buzz, 294, 0.4, 0.3)
