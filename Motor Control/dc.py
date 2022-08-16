#assuming input are normalised to a scale of 0 to 1
#odd pins left motor even pins right motor 
#odd index pins high for forward
from cmath import pi
import RPi.GPIO as GPIO
from math import tan
import time
#car_half_width=0.05
def getInput():
    return input()
def forward(val):
    if val<threshold:
        return
    GPIO.output(controller_f[0],1)
    GPIO.output(controller_f[1],0)
    GPIO.output(controller_f[2],1)
    GPIO.output(controller_f[3],0)
    GPIO.output(controller_m[0],1)
    GPIO.output(controller_m[1],0)
    GPIO.output(controller_m[2],1)
    GPIO.output(controller_m[3],0)
    GPIO.output(controller_b[0],1)
    GPIO.output(controller_b[1],0)
    GPIO.output(controller_b[2],1)
    GPIO.output(controller_b[3],0)

    dc=(val-threshold/(1-threshold))*100
    pwm_f[0].ChangeDutyCycle(dc)
    pwm_f[1].ChangeDutyCycle(dc)
    pwm_f[2].ChangeDutyCycle(dc)
    pwm_f[3].ChangeDutyCycle(dc)
    pwm_m[0].ChangeDutyCycle(dc)
    pwm_m[1].ChangeDutyCycle(dc)
    pwm_m[2].ChangeDutyCycle(dc)
    pwm_m[3].ChangeDutyCycle(dc)
    pwm_b[0].ChangeDutyCycle(dc)
    pwm_b[1].ChangeDutyCycle(dc)
    pwm_b[2].ChangeDutyCycle(dc)
    pwm_b[3].ChangeDutyCycle(dc)

def backward(val):
    if val<threshold:
        return
    GPIO.output(controller_f[0],0)
    GPIO.output(controller_f[1],1)
    GPIO.output(controller_f[2],0)
    GPIO.output(controller_f[3],1)
    GPIO.output(controller_m[0],0)
    GPIO.output(controller_m[1],1)
    GPIO.output(controller_m[2],0)
    GPIO.output(controller_m[3],1)
    GPIO.output(controller_b[0],0)
    GPIO.output(controller_b[1],1)
    GPIO.output(controller_b[2],0)
    GPIO.output(controller_b[3],1)

    dc=(val-threshold/(1-threshold))*100
    pwm_f[0].ChangeDutyCycle(dc)
    pwm_f[1].ChangeDutyCycle(dc)
    pwm_f[2].ChangeDutyCycle(dc)
    pwm_f[3].ChangeDutyCycle(dc)
    pwm_m[0].ChangeDutyCycle(dc)
    pwm_m[1].ChangeDutyCycle(dc)
    pwm_m[2].ChangeDutyCycle(dc)
    pwm_m[3].ChangeDutyCycle(dc)
    pwm_b[0].ChangeDutyCycle(dc)
    pwm_b[1].ChangeDutyCycle(dc)
    pwm_b[2].ChangeDutyCycle(dc)
    pwm_b[3].ChangeDutyCycle(dc)

def right(val):
    if val<threshold:
        return
    #turn_rad=abs(tan((val-threshold)/(1-threshold)*pi/2))
    #dc_delta=50*car_half_width/turn_rad
    dc=(val-threshold/(1-threshold))*100
    GPIO.output(controller_f[0],1)
    GPIO.output(controller_f[1],0)
    GPIO.output(controller_f[2],0)
    GPIO.output(controller_f[3],1)
    GPIO.output(controller_b[0],1)
    GPIO.output(controller_b[1],0)
    GPIO.output(controller_b[2],0)
    GPIO.output(controller_b[3],1) #fast stop mid motors
    GPIO.output(controller_m[0],1)
    GPIO.output(controller_m[1],1)
    GPIO.output(controller_m[2],1)
    GPIO.output(controller_m[3],1)

    pwm_f[0].ChangeDutyCycle(dc)
    pwm_f[1].ChangeDutyCycle(dc)
    pwm_f[2].ChangeDutyCycle(dc)
    pwm_f[3].ChangeDutyCycle(dc)
    pwm_b[0].ChangeDutyCycle(dc)
    pwm_b[1].ChangeDutyCycle(dc)
    pwm_b[2].ChangeDutyCycle(dc)
    pwm_b[3].ChangeDutyCycle(dc)
    pwm_m[0].ChangeDutyCycle(0)
    pwm_m[1].ChangeDutyCycle(0)
    pwm_m[2].ChangeDutyCycle(0)
    pwm_m[3].ChangeDutyCycle(0) #left motors faster than right
    #define turning radius based on value and use bot dimensions for differential drive
def left(val):
    if val<threshold:
        return
    #turn_rad=abs(tan((val-threshold)/(1-threshold)*pi/2))
    #dc_delta=50*car_half_width/turn_rad
    dc=(val-threshold/(1-threshold))*100
    GPIO.output(controller_f[0],0)
    GPIO.output(controller_f[1],1)
    GPIO.output(controller_f[2],1)
    GPIO.output(controller_f[3],0)
    GPIO.output(controller_b[0],0)
    GPIO.output(controller_b[1],1)
    GPIO.output(controller_b[2],1)
    GPIO.output(controller_b[3],0)
    GPIO.output(controller_m[0],1)
    GPIO.output(controller_m[1],1)
    GPIO.output(controller_m[2],1)
    GPIO.output(controller_m[3],1)

    pwm_f[0].ChangeDutyCycle(dc)
    pwm_f[1].ChangeDutyCycle(dc)
    pwm_f[2].ChangeDutyCycle(dc)
    pwm_f[3].ChangeDutyCycle(dc)
    pwm_b[0].ChangeDutyCycle(dc)
    pwm_b[1].ChangeDutyCycle(dc)
    pwm_b[2].ChangeDutyCycle(dc)
    pwm_b[3].ChangeDutyCycle(dc)
    pwm_m[0].ChangeDutyCycle(0)
    pwm_m[1].ChangeDutyCycle(0)
    pwm_m[2].ChangeDutyCycle(0)
    pwm_m[3].ChangeDutyCycle(0) #right motors faster than left
def stop():
    GPIO.output(controller_f[0],1)
    GPIO.output(controller_f[1],1)
    GPIO.output(controller_f[2],1)
    GPIO.output(controller_f[3],1)
    GPIO.output(controller_b[0],1)
    GPIO.output(controller_b[1],1)
    GPIO.output(controller_b[2],1)
    GPIO.output(controller_b[3],1)
    GPIO.output(controller_m[0],1)
    GPIO.output(controller_m[1],1)
    GPIO.output(controller_m[2],1)
    GPIO.output(controller_m[3],1)
    

#main
if __name__ == '__main__':
    try:
        print('start')
        threshold=0.1
        controller_f=(3,5,8,10) #front 
        controller_m=(19,21,22,24) # mid
        controller_b=(29,31,36,38) #back

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([controller_f[0],controller_f[1],controller_f[2],controller_f[3]],GPIO.OUT)
        GPIO.setup([controller_m[0],controller_m[1],controller_m[2],controller_m[3]],GPIO.OUT)
        GPIO.setup([controller_b[0],controller_b[1],controller_b[2],controller_b[3]],GPIO.OUT)
        print('pwm init')
        pwm_f=(GPIO.PWM(controller_f[0],300),GPIO.PWM(controller_f[1],300),GPIO.PWM(controller_f[2],300),GPIO.PWM(controller_f[3],300))
        pwm_m=(GPIO.PWM(controller_m[0],300),GPIO.PWM(controller_m[1],300),GPIO.PWM(controller_m[2],300),GPIO.PWM(controller_m[3],300))
        pwm_b=(GPIO.PWM(controller_b[0],300),GPIO.PWM(controller_b[1],300),GPIO.PWM(controller_b[2],300),GPIO.PWM(controller_b[3],300))

        for i in range(3):
            stop()
            print('loop')
            forward(0.5)
#            stop()
            time.sleep(1)
            stop()
            time.sleep(1)
            backward(0.5)
            time.sleep(1)
    except Exception as e:
        print('error',e)
        stop()
        exit(1)
    finally:
        GPIO.cleanup()
